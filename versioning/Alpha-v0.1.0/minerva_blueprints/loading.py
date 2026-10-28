"""Restricted data-only YAML/JSON loading and portable path resolution."""
from pathlib import Path
import copy
import json
import math
import re
import yaml

MAX_DOCUMENT_BYTES = 8 * 1024 * 1024


class InputError(ValueError):
    pass


class UniqueKeyLoader(yaml.SafeLoader):
    """JSON scalar subset of YAML, without aliases or implicit timestamps."""
    yaml_implicit_resolvers = copy.deepcopy(yaml.SafeLoader.yaml_implicit_resolvers)


for first, resolvers in list(UniqueKeyLoader.yaml_implicit_resolvers.items()):
    UniqueKeyLoader.yaml_implicit_resolvers[first] = [
        (tag, pattern) for tag, pattern in resolvers
        if tag not in {'tag:yaml.org,2002:bool', 'tag:yaml.org,2002:int',
                       'tag:yaml.org,2002:float', 'tag:yaml.org,2002:timestamp',
                       'tag:yaml.org,2002:null'}
    ]
UniqueKeyLoader.add_implicit_resolver('tag:yaml.org,2002:bool', re.compile(r'^(?:true|false)$'), list('tf'))
UniqueKeyLoader.add_implicit_resolver('tag:yaml.org,2002:null', re.compile(r'^null$'), ['n'])
UniqueKeyLoader.add_implicit_resolver('tag:yaml.org,2002:int', re.compile(r'^-?(?:0|[1-9][0-9]*)$'), list('-0123456789'))
UniqueKeyLoader.add_implicit_resolver('tag:yaml.org,2002:float', re.compile(r'^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+(?:[eE][+-]?[0-9]+)?|[eE][+-]?[0-9]+)$'), list('-0123456789'))


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str):
            raise InputError('Mapping keys must be strings.')
        if key in result:
            raise InputError(f'Duplicate mapping key {key!r} at line {key_node.start_mark.line + 1}.')
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueKeyLoader.add_constructor('tag:yaml.org,2002:map', unique_mapping)


def read_yaml(path: Path) -> dict:
    raw = path.read_bytes()
    if len(raw) > MAX_DOCUMENT_BYTES:
        raise InputError('Document exceeds the 8 MiB supported limit.')
    text = raw.decode('utf-8')
    for token in yaml.scan(text):
        if isinstance(token, (yaml.tokens.AliasToken, yaml.tokens.AnchorToken, yaml.tokens.TagToken)):
            raise InputError('Aliases, anchors and explicit tags are outside the Minerva YAML profile.')
    data = yaml.load(text, Loader=UniqueKeyLoader)
    if not isinstance(data, dict):
        raise InputError('The document root must be a mapping.')
    def finite(value):
        if isinstance(value, float) and not math.isfinite(value):
            raise InputError('Non-finite numbers are not supported.')
        if isinstance(value, dict):
            for item in value.values(): finite(item)
        elif isinstance(value, list):
            for item in value: finite(item)
    finite(data)
    return data


def read_json(path: Path) -> dict:
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result: raise InputError(f'Duplicate JSON key {key!r}.')
            result[key] = value
        return result
    def invalid_constant(value): raise InputError('Non-finite JSON number ' + value)
    raw = path.read_bytes()
    if len(raw) > MAX_DOCUMENT_BYTES: raise InputError('Document exceeds the 8 MiB supported limit.')
    return json.loads(raw.decode('utf-8'), object_pairs_hook=pairs, parse_constant=invalid_constant)


def safe_path(root: Path, relative: str) -> Path:
    if not isinstance(relative, str) or not relative or '\\' in relative:
        raise InputError('A nonempty portable relative path is required.')
    part = Path(relative)
    if part.is_absolute() or '..' in part.parts or re.match(r'^[A-Za-z]:', relative):
        raise InputError('Paths must stay within the declared project root.')
    target = (root / part).resolve()
    if not target.is_relative_to(root.resolve()):
        raise InputError('A path or symlink escapes the declared project root.')
    return target

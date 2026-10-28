"""Inspect source bytes and lexical Python names without executing code."""
import ast
import hashlib
from .loading import InputError, safe_path

def resolve_python_symbol(tree, symbol):
    """Resolve a qualified class/function path through lexical AST ownership."""
    current = tree
    for segment in symbol.split('.'):
        if not segment.isidentifier():
            return False
        current = next((node for node in getattr(current, 'body', [])
            if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef))
            and node.name == segment), None)
        if current is None:
            return False
    return True



class CodeInspectionMixin:
    def source_code(self, path, data):
        source = data['source']
        try: code = safe_path(self.root, source['path'])
        except InputError as error:
            self.add('PATH_INVALID', path, 'source/path', str(error)); return
        if source['state'] == 'planned' and source['sha256'] is not None:
            self.add('PLANNED_HASH', path, 'source/sha256', 'A planned source has no observed hash.')
        if not self.verify_code: return
        self.report['code_check'] = 'requested'
        if not code.is_file():
            self.add('CODE_UNAVAILABLE', path, 'source/path', 'Source unavailable for the requested code check.', 'inconclusive'); return
        self.report['counts']['code_files'] += 1
        digest = hashlib.sha256(code.read_bytes()).hexdigest()
        if source['state'] != 'observed' or source['sha256'] is None:
            self.add('CODE_NOT_OBSERVED', path, 'source', 'Present source is not covered by an observed snapshot.', 'inconclusive')
        elif digest != source['sha256']:
            self.add('CODE_HASH_MISMATCH', path, 'source/sha256', 'Current bytes differ from the observed snapshot.')
        if source['language'] != 'python':
            self.add('CODE_LANGUAGE_UNSUPPORTED', path, 'source/language', 'Hash checked; symbol inspection supports Python only.', 'warning'); return
        try: tree = ast.parse(code.read_text(encoding='utf-8'))
        except (OSError, SyntaxError, UnicodeError) as error:
            self.add('CODE_PARSE', path, 'source/path', str(error)); return
        declared = {unit['code_name'] for unit in data['units'] if unit['kind'] in ('class', 'function')}
        actual = {node.name for node in tree.body if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef))}
        if declared != actual:
            self.add('CODE_UNITS', path, 'units', f'Declared top-level names {sorted(declared)} differ from {sorted(actual)}.')
        for unit in data['units']:
            if unit['kind'] != 'class': continue
            node = next((node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == unit['code_name']), None)
            if node:
                methods = {n.name for n in node.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
                described = {op['code_name'] for op in unit['operations']}
                if methods != described:
                    self.add('CODE_METHODS', path, unit['id'], f'Declared methods {sorted(described)} differ from {sorted(methods)}.')

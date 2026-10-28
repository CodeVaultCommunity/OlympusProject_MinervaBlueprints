#!/usr/bin/env python3
"""Render the eight bilingual project assets from editable SVG source.

Requires Python 3.10+, CairoSVG 2.8.2 and DejaVu Sans fonts.
Run from any working directory: python assets/sources/render_images.py
No network access, image generation or repository-specific tooling is used.

Visual conventions and SVG helpers adapted from Atlas Specifications
(CodeVaultCommunity/OlympusProject_AtlasSpecifications, Stable-v1.0.0).
Copyright (c) 2026 Douglas de Oliveira Alkimim.
See ATLAS-LICENSE.txt for the preserved MIT notice.
"""
from pathlib import Path
import base64
import html
import shutil
import cairosvg

PROJECT = 'minerva'
HERE = Path(__file__).resolve().parent
ASSETS = HERE.parent
VERSION = 'Alpha-v0.1.0'
NAVY = '#0b1d36'
INK = '#15314f'
MUTED = '#415e78'
BLUE = '#1576cb'
CYAN = '#009db8'
TEAL = '#007786'
EDGE = '#297fbb'
PALE = '#eef8ff'
WHITE = '#ffffff'


def text(x, y, value, size=24, color=INK, weight=400, anchor='start', **attrs):
    extra = ' '.join(f'{k.replace("_", "-")}="{html.escape(str(v), quote=True)}"' for k, v in attrs.items())
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}" {extra}>{html.escape(value)}</text>'


def lines(x, y, values, size=23, color=INK, gap=35, **attrs):
    return ''.join(text(x, y + i * gap, v, size=size, color=color, **attrs) for i, v in enumerate(values))


def rect(x, y, w, h, fill=WHITE, stroke='#9cc9df', radius=18, width=2.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>'


def arrow(d, dashed=False):
    dash = ' stroke-dasharray="10 8"' if dashed else ''
    return f'<path d="{d}" fill="none" stroke="{EDGE}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#arrow)"{dash}/>'


def tag(cx, cy, label, width=250, size=20):
    return rect(cx-width/2, cy-20, width, 40, '#f4fbff', '#c4dfed', 10, 2) + text(cx, cy+7, label, size=size, anchor='middle')


def icon(kind, x, y, color=BLUE, size=38):
    paths = {
        'layers': '<path d="M4 12 20 3 36 12 20 21Z M4 20 20 29 36 20 M4 28 20 37 36 28"/>',
        'model': '<rect x="3" y="3" width="11" height="11" rx="2"/><rect x="26" y="3" width="11" height="11" rx="2"/><rect x="15" y="27" width="11" height="11" rx="2"/><path d="M8.5 14v7H31.5v-7 M20.5 21v6"/>',
        'document': '<path d="M9 3H25l8 8v26H9Z M25 3v9h8 M15 19h12 M15 25h12 M15 31h8"/>',
        'code': '<path d="m13 8-10 12 10 12 M27 8l10 12-10 12 M24 3l-8 34"/>',
        'check': '<circle cx="20" cy="20" r="17"/><path d="m11 20 6 7 13-15"/>',
        'evidence': '<path d="M8 3h24v34H8Z M14 12h12 M14 19h12 M14 27l4 4 8-9"/>',
        'tool': '<path d="M24 4a10 10 0 0 0-11 13L3 27a6 6 0 0 0 9 9l10-10A10 10 0 0 0 36 15l-9 7-8-8Z"/>',
        'case': '<rect x="3" y="10" width="34" height="26" rx="3"/><path d="M13 10V4h14v6 M3 21h34 M17 18h6v7h-6Z"/>',
        'boundary': '<rect x="4" y="4" width="32" height="32" rx="4"/><path d="M1 20h22 M17 14l6 6-6 6 M29 10v20"/>',
    }
    return f'<g transform="translate({x} {y}) scale({size/40})" fill="none" stroke="{color}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">{paths.get(kind, paths["document"])}</g>'


def heading(x, y, label, kind='document', color=BLUE, size=27):
    return icon(kind, x, y-30, color) + text(x+57, y, label, size=size, color=color, weight=700)


def raster(name, x, y, w, h, mode='meet'):
    payload = base64.b64encode((HERE/name).read_bytes()).decode('ascii')
    return f'<image x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="xMidYMid {mode}" xlink:href="data:image/png;base64,{payload}"/>'


def svg(w, h, body, title, description, rounded=False):
    clip = '<clipPath id="banner-clip"><rect width="1600" height="534" rx="40"/></clipPath>' if rounded else ''
    group = '<g clip-path="url(#banner-clip)">' if rounded else '<g>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="asset-title asset-description">
<title id="asset-title">{html.escape(title)}</title>
<desc id="asset-description">{html.escape(description)}</desc>
<defs>
<marker id="arrow" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M1 1 L11 6 L1 11 Z" fill="{EDGE}"/></marker>
<linearGradient id="brand-title"><stop offset="0" stop-color="#ffffff"/><stop offset=".56" stop-color="#e6faff"/><stop offset="1" stop-color="#67dbfa"/></linearGradient>
{clip}</defs>
<g font-family="DejaVu Sans,Arial,sans-serif">{group}{body}</g></g>
</svg>'''


def banner(pt=False):
    is_minerva = PROJECT == 'minerva'
    name = 'Minerva' if is_minerva else 'Vulcan'
    second = 'Blueprints' if is_minerva else 'Ecosystem'
    layer = 'L2' if is_minerva else 'L3'
    if is_minerva:
        subtitle = 'Modelos de programa. Verificação explícita.' if pt else 'Program models. Explicit verification.'
        detail = 'ADMV    ·    ADPM + ADVS'
    else:
        subtitle = 'Organização do código. Realização concreta.' if pt else 'Code organization. Concrete realization.'
        detail = 'ADI    ·    ARQUITETURA + IMPLEMENTAÇÃO' if pt else 'ADI    ·    ARCHITECTURE + IMPLEMENTATION'
    b = rect(0,0,1600,534,'#061525','#061525',0,0)
    b += raster(f'{PROJECT}-hero-art.png',0,0,1600,534,mode='slice')
    b += raster('olympus-icon-original.png',70,47,66,66)
    b += text(156,91,f'OLYMPUS PROJECT  /  OAL {layer}',19,'#bddcec',600,letter_spacing='.8')
    b += raster(f'{PROJECT}-icon-original.png',63,151,194,194)
    b += text(287,231,name,80,'url(#brand-title)',700,letter_spacing='-1.5')
    b += text(289,301,second,54,'url(#brand-title)',600,letter_spacing='-1')
    b += text(78,386,subtitle,24,'#c0dce9')
    b += text(78,434,detail,18,'#80e8ef',600,letter_spacing='.6')
    b += text(78,487,VERSION,16,'#afc6d7')
    description = ('Header decorativo; os símbolos originais são preservados. ' if pt else 'Decorative header; the supplied original icons are preserved. ') + f'{name} {second}, Olympus Project, OAL {layer}, {VERSION}.'
    return svg(1600,534,b,f'{name} {second} · {VERSION}',description,rounded=True)


def oal_position(pt=False):
    m = PROJECT == 'minerva'
    if m:
        top = 'OAL L2 · ADMV'
        top_lines = ['Modelagem do programa e especificação da verificação.'] if pt else ['Program modeling and specification of verification.']
        name = 'Minerva Blueprints'
        model_lines = ['Modelo abstrato de projeto e verificação do programa.', 'Semântica independente da representação escolhida.'] if pt else ['Abstract model of program design and verification.', 'Semantics independent of the selected representation.']
        left_title = 'ADPM · Modelo do programa' if pt else 'ADPM · Program model'
        left_lines = ['Casos, entidades e contratos de ferramentas.', 'Comportamento, dependências e composição.'] if pt else ['Cases, entities and tool contracts.', 'Behavior, dependencies and composition.']
        right_title = 'ADVS · Modelo de verificação' if pt else 'ADVS · Verification model'
        right_lines = ['Cenários, resultados esperados e critérios.', 'Plano identificado por caso de programa.'] if pt else ['Scenarios, expected outcomes and criteria.', 'A plan identified by program case.']
        branch = ('Programa','Verificação') if pt else ('Program design','Verification plan')
        bottom = 'Blueprints concretos de projeto' if pt else 'Concrete project blueprints'
        bottom_lines = ['IDs, versões, vínculos e perfis declarados.', 'O espelho YAML por arquivo é uma representação em L2.'] if pt else ['Declared IDs, versions, links and profiles.', 'The per-file YAML mirror is a representation in L2.']
        lower = ('Modelo','Plano') if pt else ('Model','Plan')
    else:
        top = 'OAL L3 · ADI'
        top_lines = ['Obrigações para organização e implementação de programas.'] if pt else ['Obligations for program organization and implementation.']
        name = 'Vulcan Ecosystem'
        model_lines = ['Organização e realização concreta dos aplicativos.', 'Independente de linguagem ou biblioteca obrigatória.'] if pt else ['Organization and concrete realization of applications.', 'Independent of a language or a mandatory library.']
        left_title = 'Ecossistema de aplicativos' if pt else 'Application ecosystem'
        left_lines = ['Um aplicativo por diretório em apps/.', 'Linguagens e arquiteturas podem diferir.'] if pt else ['One application per directory in apps/.', 'Languages and architectures may differ.']
        right_title = 'Vulcan Architecture'
        right_lines = ['Perfil recomendado para um aplicativo.', 'Use cases · tools · entities · value objects.'] if pt else ['Recommended profile for an application.', 'Use cases · tools · entities · value objects.']
        branch = ('Organização','Perfil recomendado') if pt else ('Organization','Recommended profile')
        bottom = 'Realização concreta' if pt else 'Concrete realization'
        bottom_lines = ['Perfis declarados, composição, modos e evidências.', 'Os registros L3 referenciam os blueprints L2 selecionados.'] if pt else ['Declared profiles, composition, modes and evidence.', 'L3 records reference the selected L2 blueprints.']
        lower = ('Adoção','Realização') if pt else ('Adoption','Realization')
    b = rect(60,35,1280,130,PALE,'#80bddb')
    b += heading(95,85,top,'layers',size=30)
    b += lines(150,131,top_lines,size=25)
    b += arrow('M700 166V267') + tag(700,214,'Conformidade' if pt else 'Conformance',240)
    b += rect(190,280,1020,170,NAVY,CYAN)
    b += heading(230,335,name,'model','#80e8ef',31)
    b += lines(230,382,model_lines,24,'#e4f2ff',35)
    b += arrow('M420 451V505H365V548')
    b += arrow('M980 451V505H1035V548')
    b += tag(365,499,branch[0],280) + tag(1035,499,branch[1],300)
    b += rect(60,560,610,185)
    b += heading(90,612,left_title,'model',size=25)
    b += lines(90,660,left_lines,23,MUTED,36)
    b += rect(730,560,610,185,'#f0fcfc','#8acfd2')
    b += heading(760,612,right_title,'check' if m else 'code',TEAL,25)
    b += lines(760,660,right_lines,23,MUTED,36)
    b += arrow('M365 746V803H520V858')
    b += arrow('M1035 746V803H880V858')
    b += tag(365,797,lower[0],210) + tag(1035,797,lower[1],210)
    b += rect(150,870,1100,175,PALE,'#80bddb')
    b += heading(190,927,bottom,'document',size=28)
    b += lines(190,974,bottom_lines,24,INK,35)
    description = ('Posição do modelo no OAL e relações semânticas entre suas partes e os artefatos concretos. As setas não indicam geração automática.' if pt else 'Position of the model in OAL and semantic relationships between its parts and concrete artifacts. The arrows do not imply automatic generation.')
    return svg(1400,1080,b,f'{name} · '+('posição OAL' if pt else 'OAL position'),description)


def minerva_model(pt=False):
    b = rect(60,35,610,250)
    b += heading(90,88,'ADPM · Programa' if pt else 'ADPM · Program','model',size=28)
    b += lines(90,140,['Casos, entidades e contratos de ferramentas.','Regras, comportamento e dependências.','Composição, ator e autorização.'] if pt else ['Cases, entities and tool contracts.','Rules, behavior and dependencies.','Composition, actor and authorization.'],23,MUTED,39)
    b += rect(730,35,610,250,'#f0fcfc','#8acfd2')
    b += heading(760,88,'ADVS · Verificação' if pt else 'ADVS · Verification','check',TEAL,28)
    b += lines(760,140,['Cenários e resultados esperados.','Critérios, fixtures e efeitos.','Um teste comportamental lógico por caso.'] if pt else ['Scenarios and expected outcomes.','Criteria, fixtures and effects.','One logical behavioral test per case.'],23,MUTED,39)
    b += arrow('M365 286V332H570V377') + arrow('M1035 286V332H830V377')
    b += tag(365,329,'Modelo' if pt else 'Model',220) + tag(1035,329,'Plano' if pt else 'Plan',220)
    b += rect(170,390,1060,185,NAVY,CYAN)
    b += heading(210,447,'Um blueprint de projeto' if pt else 'One project blueprint','model','#80e8ef',29)
    b += lines(210,497,['IDs lógicos estáveis, versões, contratos de origem e vínculos.','ADPM e ADVS conectadas, com identidades recuperáveis.'] if pt else ['Stable logical IDs, versions, source contracts and semantic links.','ADPM and ADVS stay connected and independently identifiable.'],23,'#e4f2ff',37)
    b += arrow('M700 576V682') + tag(700,629,'Perfil YAML' if pt else 'YAML profile',240)
    b += rect(60,695,1280,350,PALE,'#80bddb')
    b += heading(95,750,'Espelho por arquivo · L2' if pt else 'Per-file mirror · L2','document',size=28)
    b += text(95,802,'apps/<App>/<path>/<File.ext>',23,INK,font_family='DejaVu Sans Mono,monospace')
    b += text(95,843,'docs/L2_MinervaBlueprints/apps/<App>/<path>/<File.ext>.yaml',23,TEAL,font_family='DejaVu Sans Mono,monospace')
    b += text(100,901,'Estado da fonte' if pt else 'Source state',22,BLUE,700)
    b += text(100,936,'planned  ·  observed',21)
    b += text(100,974,'Natureza do documento' if pt else 'Document nature',22,BLUE,700)
    b += text(100,1009,'designed  ·  reconstructed  ·  mixed',21)
    b += text(760,901,'Unidades identificadas' if pt else 'Identified units',22,TEAL,700)
    b += lines(760,936,['Uma classe/struct ou várias unidades legadas.','Contratos, dependências e comportamento.','Vínculos com ADPM, ADVS e fontes.'] if pt else ['One class/struct, or several legacy units.','Contracts, dependencies and behavior.','Links to ADPM, ADVS and source files.'],21,INK,35)
    b += rect(60,1090,1280,60,'#f8fcff','#c4dfed',14,2)
    b += text(700,1128,'docs/ é recomendada; Shared/ reúne apoio transversal e não constitui uma camada OAL.' if pt else 'docs/ is recommended; Shared/ provides cross-cutting support, not a new OAL layer.',21,MUTED,anchor='middle')
    desc = ('ADPM e ADVS formam o modelo L2. Um blueprint identifica contratos e cenários. O perfil YAML espelha arquivos em L2, identifica estado e origem e suporta múltiplas unidades legadas.' if pt else 'ADPM and ADVS form the L2 model. A blueprint identifies contracts and scenarios. The YAML profile mirrors files in L2, records state and origin, and supports several legacy units.')
    return svg(1400,1180,b,'Minerva Blueprints · '+('conteúdo do modelo' if pt else 'model content'),desc)


def vulcan_model(pt=False):
    b = rect(60,35,1280,140,NAVY,CYAN)
    b += heading(100,91,'Vulcan Ecosystem · apps/','model','#80e8ef',30)
    b += text(100,138,'Cada app declara arquitetura, linguagem e modos de execução.' if pt else 'Each application declares its architecture, language and execution modes.',25,'#e4f2ff')
    b += arrow('M420 176V230H365V278') + arrow('M980 176V230H1035V278')
    b += tag(365,228,'Perfil selecionado' if pt else 'Selected profile',250) + tag(1035,228,'Aplicativo existente' if pt else 'Existing application',270)
    b += rect(60,290,610,275)
    b += heading(90,343,'App A · Vulcan Architecture','code',size=25)
    b += lines(90,395,['Use cases agrupados por domínio.','Tools · entities · value objects.','Composição explícita; bibliotecas opcionais.','Uma classe/struct principal por arquivo.'] if pt else ['Use cases grouped by domain.','Tools · entities · value objects.','Explicit composition; optional libraries.','One main class/struct per file.'],23,MUTED,38)
    b += rect(730,290,610,275,'#f0fcfc','#8acfd2')
    b += heading(760,343,'App B · Outra arquitetura' if pt else 'App B · Another architecture','case',TEAL,25)
    b += lines(760,395,['Aplicativo existente ou novo.','Linguagem e organização internas próprias.','Contratos públicos e execução declarados.','Conformidade limitada ao perfil adotado.'] if pt else ['Existing or newly developed application.','Its own language and internal design.','Public contracts and execution declared.','Conformance scoped to its adopted profile.'],23,MUTED,38)
    b += arrow('M365 566V610H500V647') + arrow('M1035 566V610H900V647')
    b += rect(310,660,780,105,'#f0fcfc','#8acfd2')
    b += text(700,700,'Integração pública, quando presente' if pt else 'Public integration, when present',25,TEAL,700,anchor='middle')
    b += text(700,739,'Contratos públicos; mapeamentos de interação continuam em L4.' if pt else 'Declared contracts; interaction mappings retain their L4 identity.',21,INK,anchor='middle')
    b += arrow('M700 766V847') + tag(700,806,'Registrar e referenciar' if pt else 'Record and reference',300)
    b += rect(60,860,1280,230,PALE,'#80bddb')
    b += heading(95,916,'Registros da realização concreta · L3' if pt else 'Concrete realization records · L3','evidence',size=28)
    b += text(95,963,'docs/L3_Vulcan/',24,TEAL,font_family='DejaVu Sans Mono,monospace')
    b += lines(95,1008,['Inventário e perfis · composição e decisões técnicas.','Modos e comandos · integrações selecionadas · evidências de execução.'] if pt else ['App inventory and profiles · composition and technical decisions.','Modes and commands · selected integrations · execution evidence.'],24,INK,37)
    b += rect(60,1120,1280,50,'#f8fcff','#c4dfed',14,2)
    b += text(700,1152,'Local recomendado: docs/L3_Vulcan/ · blueprints por arquivo permanecem em L2.' if pt else 'Recommended location: docs/L3_Vulcan/ · per-file blueprints stay in L2.',21,MUTED,anchor='middle')
    desc = ('Um ecossistema pode conter apps Vulcan e apps com outras arquiteturas. Contratos públicos sustentam a comunicação quando presente. L3 documenta inventário, composição, execução, integrações concretas e evidências; o espelho permanece em L2.' if pt else 'An ecosystem may contain Vulcan applications and applications with other architectures. Public contracts support communication when present. L3 records inventory, composition, execution, concrete integrations and evidence; the mirror stays in L2.')
    return svg(1400,1200,b,'Vulcan Ecosystem · '+('organização e registros' if pt else 'organization and records'),desc)


def workflow(pt=False):
    m = PROJECT == 'minerva'
    if m:
        name = 'Minerva Blueprints'
        title1 = 'Contratos de origem selecionados · L1' if pt else 'Selected source contracts · L1'
        lines1 = ['Atlas Specifications, quando adotado, com versão e escopo fixados.'] if pt else ['Atlas Specifications, when adopted, with a fixed version and scope.']
        title2 = 'Modelar ADPM e ADVS · L2' if pt else 'Model ADPM and ADVS · L2'
        lines2 = ['Preservar contratos; explicitar decisões e pendências.','Conectar comportamento, cenários, resultados esperados e vínculos.'] if pt else ['Preserve contracts; make decisions and pending issues explicit.','Connect behavior, scenarios, expected outcomes and source links.']
        title3 = 'Revisar o blueprint' if pt else 'Review the blueprint'
        lines3 = ['Verificar IDs, contratos, referências e critérios de verificação.','Revisão manual ou apoiada por ferramentas declaradas.'] if pt else ['Check IDs, contracts, references and verification criteria.','Review manually or with declared supporting tools.']
        lefttitle = 'Realizar · L3' if pt else 'Realize · L3'
        leftlines = ['Código e testes derivados','do modelo selecionado.','A realização executa.'] if pt else ['Code and tests derived','from the selected model.','The realization executes.']
        righttitle = 'Evidências · L3' if pt else 'Evidence · L3'
        rightlines = ['Resultados e limites observados.','Vínculos com cenários ADVS.','Diferenças alimentam revisão.'] if pt else ['Observed results and limits.','Links to ADVS scenarios.','Differences inform review.']
        foot = 'Fluxo de trabalho com revisão explícita; as setas não prometem geração automática.' if pt else 'A workflow with explicit review; the arrows do not promise automatic generation.'
        feedback = 'Revisar diferenças' if pt else 'Review differences'
        feedbackpath = 'M1085 1031V1100H150V363H286'
    else:
        name = 'Vulcan Ecosystem'
        title1 = 'Blueprints e contratos selecionados · L2' if pt else 'Selected blueprints and contracts · L2'
        lines1 = ['Minerva, quando adotado: modelo, ADVS, versões e escopo declarados.'] if pt else ['Minerva, when adopted: model, ADVS, declared versions and scope.']
        title2 = 'Implementar e compor · L3' if pt else 'Implement and compose · L3'
        lines2 = ['Aplicar perfis; compor ferramentas concretas e recursos.','Preservar contratos, autorização e efeitos observáveis.'] if pt else ['Apply profiles; compose concrete tools and resources.','Preserve contracts, authorization and observable effects.']
        title3 = 'Selecionar apps e modos de execução' if pt else 'Select applications and execution modes'
        lines3 = ['Inicializador, configuração e dependências de partida declarados.','Prontidão e encerramento pertencem ao modo selecionado.'] if pt else ['Declared launcher, configuration and startup dependencies.','Readiness and shutdown belong to the selected mode.']
        lefttitle = 'Executar e verificar' if pt else 'Run and verify'
        leftlines = ['Testes derivados da ADVS.','Núcleo e mapeamentos públicos','verificados no escopo declarado.'] if pt else ['Tests derived from ADVS.','Core and public mappings','checked in the declared scope.']
        righttitle = 'Registrar evidências' if pt else 'Record evidence'
        rightlines = ['Revisão, ambiente e comandos.','Resultados e limites.','docs/L3_Vulcan/evidence/'] if pt else ['Revision, environment, commands.','Results and limits.','docs/L3_Vulcan/evidence/']
        foot = 'A evidência descreve o observado; o plano de verificação preserva sua identidade em L2.' if pt else 'Evidence describes observations; the verification plan keeps its identity in L2.'
        feedback = 'Revisar impacto' if pt else 'Review impact'
        feedbackpath = 'M1085 1031V1100H150V103H286'
    b = rect(300,30,1000,145,PALE,'#80bddb')
    b += heading(335,86,title1,'document',size=27)
    b += lines(335,136,lines1,23)
    b += arrow('M800 176V262') + tag(800,219,'Entrada versionada' if pt else 'Versioned input',280)
    b += rect(300,275,1000,175,NAVY,CYAN)
    b += heading(335,333,title2,'model' if m else 'code','#80e8ef',29)
    b += lines(335,382,lines2,23,'#e4f2ff',37)
    b += arrow('M800 451V542') + tag(800,496,'Revisão explícita' if pt else 'Explicit review',260)
    b += rect(300,555,1000,145)
    b += heading(335,609,title3,'check' if m else 'tool',size=27)
    b += lines(335,654,lines3,23,MUTED,32)
    b += arrow('M800 701V748H535V787') + tag(800,748,'Realização declarada' if pt else 'Declared realization',290)
    b += rect(300,800,470,230,'#f0fcfc','#8acfd2')
    b += heading(330,855,lefttitle,'code' if m else 'check',TEAL,25)
    b += lines(330,906,leftlines,22,INK,37)
    b += arrow('M771 921H856') + tag(820,876,'Saída' if pt else 'Output',96,18)
    b += rect(870,800,430,230,PALE,'#80bddb')
    b += heading(900,855,righttitle,'evidence',BLUE,23)
    b += lines(900,906,rightlines,21,INK,37)
    b += arrow(feedbackpath,True) + tag(150,590,feedback,240,20)
    b += rect(60,1140,1280,55,'#f8fcff','#c4dfed',14,2)
    b += text(700,1175,foot,21,MUTED,anchor='middle')
    desc = ('Fluxo de trabalho proposto: entradas versionadas, modelagem ou realização, revisão explícita, execução e evidências. O retorno tracejado indica revisão das diferenças ou impactos, nunca atualização automática dos contratos.' if pt else 'Proposed workflow: versioned inputs, modeling or realization, explicit review, execution and evidence. The dashed return denotes review of differences or impacts, never automatic changes to contracts.')
    return svg(1400,1230,b,f'{name} · '+('fluxo de trabalho' if pt else 'workflow'),desc)


def main():
    for name in (PROJECT, 'olympus'):
        shutil.copyfile(HERE/f'{name}-icon-original.png',ASSETS/f'{name}-icon.png')
    for language, pt in [('en',False),('pt-br',True)]:
        generators = {
            'banner': banner,
            'oal-position': oal_position,
            'model': minerva_model if PROJECT == 'minerva' else vulcan_model,
            'workflow': workflow,
        }
        for kind, generate in generators.items():
            source = generate(pt)
            stem = f'{PROJECT}-{kind}-{language}'
            (HERE/f'{stem}.svg').write_text(source,encoding='utf-8')
            png_bytes = cairosvg.svg2png(bytestring=source.encode('utf-8'))
            temporary = ASSETS/f'.{stem}.png.tmp'
            temporary.write_bytes(png_bytes)
            temporary.replace(ASSETS/f'{stem}.png')
            print(stem + '.svg -> .png')


if __name__ == '__main__':
    main()

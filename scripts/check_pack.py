#!/usr/bin/env python3
"""Contrôles locaux en lecture seule ; ce script n'accorde aucune validation humaine."""
import argparse,json,re,datetime,os
from pathlib import Path
from urllib.parse import unquote,urlsplit

ENUMS={
 'type':{'source','proposition','reference','decision','reprise','trace','instruction'},
 'zone':{'humaine','deleguee','collaborative'},
 'authority':{'source','proposition','reference','derivee','trace','instruction'},
 'document_status':{'draft','active','completed','archived'},
 'validation_status':{'not_required','pending','approved','rejected'},
}

def metadata(text):
    """Sous-ensemble YAML strict : une clé par ligne, scalaires, listes JSON inline."""
    if not text.startswith('---\n'):raise ValueError('frontmatter absent')
    bits=text.split('\n---',1)
    if len(bits)!=2:raise ValueError('frontmatter non fermé')
    data={}
    for line in bits[0].splitlines()[1:]:
        if not line.strip():continue
        key,sep,value=line.partition(':')
        if not sep or not re.fullmatch(r'[a-z_]+',key):raise ValueError('syntaxe frontmatter non prise en charge')
        if key in data:raise ValueError('clé dupliquée '+key)
        value=value.strip()
        if value.startswith(('"','[')):
            try:value=json.loads(value)
            except json.JSONDecodeError as e:raise ValueError('valeur JSON inline invalide') from e
        data[key]=value
    return data

def governance(text):
    try:d=metadata(text)
    except ValueError as e:return [str(e)]
    errors=[]
    for key,values in ENUMS.items():
        if not isinstance(d.get(key),str) or d[key] not in values:errors.append('valeur absente ou inconnue '+key)
    for key in ['audience','sources']:
        if not isinstance(d.get(key),list) or not all(isinstance(x,str) for x in d[key]):errors.append('liste inline attendue '+key)
    audience=d.get('audience')
    if isinstance(audience,list) and all(isinstance(x,str) for x in audience) and (not audience or any(x not in {'humain','agent'} for x in audience)):errors.append('audience invalide')
    approved=d.get('validation_status')=='approved'
    if approved:
        if not d.get('validated_by'):errors.append('validateur absent')
        try:datetime.date.fromisoformat(d.get('validated_on',''))
        except (ValueError,TypeError):errors.append('date de validation invalide')
    elif d.get('validated_by') or d.get('validated_on'):errors.append('validation résiduelle sur document non approuvé')
    if d.get('authority')=='reference' and not approved:errors.append('référence sans approbation')
    if d.get('authority')=='derivee' and not d.get('sources'):errors.append('contenu dérivé sans sources')
    return errors

def check(root):
    errors=[]
    if not root.is_dir():return ['dossier racine absent']
    paths=[p for p in root.rglob('*') if '.git' not in p.relative_to(root).parts and '__pycache__' not in p.relative_to(root).parts]
    note_names={}
    for p in paths:
        rel=p.relative_to(root)
        if p.is_symlink():errors.append(f'{rel}: lien symbolique interdit dans un paquet de publication')
        if p.name in {'.env','auth.json','state.db','workspace.json'} or any(x in rel.parts for x in {'memories','sessions','.obsidian'}):errors.append(f'{rel}: fichier privé ou état local interdit')
        if p.suffix=='.md':note_names.setdefault(p.stem,[]).append(p)
    for p in sorted(q for q in paths if q.suffix=='.md' and q.is_file() and not q.is_symlink()):
        text=p.read_text(encoding='utf-8-sig')
        rel=p.relative_to(root).as_posix()
        if rel.startswith('examples/vault/') and p.name not in {'AGENTS.md','Accueil.md'}:
            errors.extend(f'{rel}: {e}' for e in governance(text))
        live=re.sub(r'```.*?```','',text,flags=re.S)
        live=re.sub(r'`[^`\n]*`','',live)
        for target in re.findall(r'\[\[([^\]]+)\]\]',live):
            name=target.split('|')[0].split('#')[0].strip()
            if not name:continue
            # Résolution bornée au mini-vault pour ses liens ; pas au vault hôte.
            scope=(root/'examples/vault' if rel.startswith('examples/vault/') else root).resolve()
            # Une cible explicite doit rester sous la racine de scope : pas de repli homonyme qui masquerait une évasion.
            name_path=Path(name)
            lexical=Path(os.path.normpath(scope/name_path))
            if name_path.is_absolute() or not lexical.is_relative_to(scope):
                errors.append(f'{rel}: wikilink hors du périmètre {name}')
                continue
            hits=[q for q in dict.fromkeys([lexical,lexical if lexical.suffix else lexical.with_suffix('.md')]) if q.is_file()]
            if not hits:
                hits=[q for q in note_names.get(Path(name).stem,[]) if q.is_relative_to(scope)]
            hits=list(dict.fromkeys(hits))
            if not hits:errors.append(f'{rel}: wikilink absent {name}')
            elif len(hits)>1:errors.append(f'{rel}: wikilink ambigu {name}')
        for target in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)\s]+)\)',live):
            u=urlsplit(target)
            if u.scheme or not u.path:continue
            q=p.parent/unquote(u.path)
            if not q.exists():errors.append(f'{p.relative_to(root)}: lien absent {target}')
    return errors

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('root',type=Path,nargs='?',default=Path(__file__).resolve().parents[1])
    args=ap.parse_args()
    errors=check(args.root.resolve())
    print(json.dumps({'errors':errors},ensure_ascii=False,indent=2))
    return 1 if errors else 0
if __name__=='__main__':raise SystemExit(main())

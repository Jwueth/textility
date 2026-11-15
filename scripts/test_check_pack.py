from pathlib import Path
import subprocess,sys,tempfile,unittest
SCRIPT=Path(__file__).resolve().parent/'check_pack.py'

def run(root):
    return subprocess.run([sys.executable,str(SCRIPT),str(root)],capture_output=True,text=True)

class PackChecks(unittest.TestCase):
    def test_finds_missing_relative_link(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            (root/'README.md').write_text('# Demo\n[Absent](missing.md)\n',encoding='utf-8')
            p=run(root)
            self.assertEqual(p.returncode,1,p.stderr)
            self.assertIn('missing.md',p.stdout)
    def test_rejects_incoherent_governance(self):
        variants=[
            'type: reference\nzone: humaine\nauthority: reference\ndocument_status: active\nvalidation_status: approved\naudience: ["humain"]\nsources: []\n',
            'type: reprise\nzone: deleguee\nauthority: derivee\ndocument_status: active\nvalidation_status: not_required\naudience: ["agent"]\nsources: []\n',
            'type: proposition\ntype: decision\nzone: inconnue\nauthority: proposition\ndocument_status: draft\nvalidation_status: pending\naudience: ["humain"]\nsources: []\n',
        ]
        for fm in variants:
            with self.subTest(fm=fm),tempfile.TemporaryDirectory() as d:
                root=Path(d);p=root/'examples/vault/00_Inbox/Note.md';p.parent.mkdir(parents=True)
                p.write_text('---\n'+fm+'---\n# Fictif\n',encoding='utf-8')
                r=run(root)
                self.assertEqual(r.returncode,1,r.stdout+r.stderr)
    def test_rejects_broken_wikilink_and_private_file(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);(root/'README.md').write_text('[[Introuvable]]\n',encoding='utf-8')
            (root/'auth.json').write_text('{}',encoding='utf-8')
            p=run(root)
            self.assertEqual(p.returncode,1,p.stdout+p.stderr)
            self.assertIn('Introuvable',p.stdout)
            self.assertIn('auth.json',p.stdout)
    def test_valid_links_and_code_examples_are_accepted_read_only(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);(root/'Cible.md').write_text('# Cible\n',encoding='utf-8')
            (root/'README.md').write_text('[Cible](Cible.md)\n[[Cible]]\n`[[Absent]]`\n```md\n[Absent](absent.md)\n```\n',encoding='utf-8')
            before={p.name:p.read_bytes() for p in root.iterdir()}
            p=run(root)
            self.assertEqual(p.returncode,0,p.stdout+p.stderr)
            self.assertEqual(before,{p.name:p.read_bytes() for p in root.iterdir()})

    def test_rejects_wikilink_escaping_mini_vault(self):
        """Un wikilink explicite ne peut pas sortir du mini-vault, même si la cible existe ailleurs."""
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            (root/'examples/vault').mkdir(parents=True)
            (root/'examples/Outside.md').write_text('# Dehors\n',encoding='utf-8')
            outside=str(root/'examples/Outside')
            cases={'relatif':'[[../Outside]]','absolu':'[['+outside+']]'}
            for label,target in cases.items():
                with self.subTest(cas=label):
                    (root/'examples/vault/Accueil.md').write_text(target+'\n',encoding='utf-8')
                    p=run(root)
                    self.assertEqual(p.returncode,1,p.stdout+p.stderr)
                    self.assertIn('Outside',p.stdout)
                    self.assertNotIn('Traceback',p.stderr)

    def test_accepts_wikilinks_resolved_inside_scope(self):
        """Liens simples, relatifs locaux, fragments et alias restent acceptés dans le mini-vault."""
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            (root/'examples/vault').mkdir(parents=True)
            (root/'examples/vault/Note.md').write_text('---\ntype: source\nzone: humaine\nauthority: source\ndocument_status: active\nvalidation_status: not_required\naudience: ["humain"]\nsources: []\n---\n# Note\n',encoding='utf-8')
            (root/'examples/vault/Accueil.md').write_text('[[Note]]\n[[./Note]]\n[[Note#Section|alias]]\n[[Note.md]]\n',encoding='utf-8')
            p=run(root)
            self.assertEqual(p.returncode,0,p.stdout+p.stderr)

    def test_malformed_audience_and_sources_report_errors(self):
        """Une liste mal typée produit des diagnostics, jamais une TypeError."""
        base='type: source\nzone: humaine\nauthority: source\ndocument_status: active\nvalidation_status: not_required\n'
        cases=[
            'audience: [{}]\nsources: []\n',
            'audience: [[]]\nsources: []\n',
            'audience: ["humain", {}]\nsources: []\n',
            'audience: [["humain"]]\nsources: []\n',
            'audience: [1]\nsources: []\n',
            'audience: "humain"\nsources: []\n',
            'audience: []\nsources: []\n',
            'audience: ["robot"]\nsources: []\n',
            'audience: ["humain"]\nsources: [{}]\n',
            'audience: ["humain"]\nsources: [[]]\n',
        ]
        for fm in cases:
            with self.subTest(fm=fm.replace('\n',' ')),tempfile.TemporaryDirectory() as d:
                root=Path(d);n=root/'examples/vault/00_Inbox/Note.md';n.parent.mkdir(parents=True)
                n.write_text('---\n'+base+fm+'---\n# Fictif\n',encoding='utf-8')
                r=run(root)
                self.assertEqual(r.returncode,1,r.stdout+r.stderr)
                self.assertNotIn('Traceback',r.stderr)
                self.assertIn('errors',r.stdout)

if __name__=='__main__':
    unittest.main()

"""Testes do contrato de distribuição e do HTML offline."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "a9-educacao"


class DistributionContract(unittest.TestCase):
    def test_complete_self_contained_skill(self):
        self.assertTrue((SKILL / "SKILL.md").is_file())
        for name in ("Contexto e Regras", "Design System", "Prompts por Setor", "Apresentações", "Plataformas e Sistemas"):
            self.assertTrue((SKILL / "references" / (name + ".md")).is_file())
        self.assertEqual((SKILL / "references" / "Prompts por Setor.md").read_text("utf-8").count("```text"), 27)
        for name in ("a9-branco.png", "a9-preto.png", "a9-colorido.png"):
            self.assertGreater((SKILL / "assets" / "logos" / name).stat().st_size, 1000)

    def test_build_and_archive_contract(self):
        module_spec = importlib.util.spec_from_file_location("a9_build", ROOT / "scripts" / "build.py")
        module = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as temp:
            archive = module.package(Path(temp))
            with zipfile.ZipFile(archive) as bundle:
                names = bundle.namelist()
                self.assertIn("a9-educacao/SKILL.md", names)
                self.assertIn("a9-educacao/references/Apresentações.md", names)
                self.assertIn("a9-educacao/references/Plataformas e Sistemas.md", names)
                self.assertTrue(all(n.startswith("a9-educacao/") for n in names))
                self.assertFalse(any(".work" in n or ".git/" in n for n in names))
                self.assertIsNone(bundle.testzip())
                self.assertTrue(all(item.create_system == 3 for item in bundle.infolist()))
                self.assertNotIn(b"\r\n", bundle.read("a9-educacao/assets/tokens/tokens.css"))
                html = bundle.read("a9-educacao/assets/apresentacoes/demo-a9.html").decode("utf-8")
                self.assertEqual(html.count('<section class="slide'), 8)
                self.assertIn("data:font/ttf;base64,", html)
                self.assertIn("data:image/png;base64,", html)
                self.assertNotIn("{{", html)
                self.assertNotRegex(html, r'(?:src|href)=["\x27]https?://')
                self.assertIn('@media print', html)
                self.assertIn('body .slide', html)
                self.assertIn('prefers-reduced-motion', html)
                self.assertIn('event.target.closest', html)

    def test_tokens_have_exact_brand_values(self):
        tokens = json.loads((SKILL / "assets" / "tokens" / "tokens.json").read_text("utf-8"))
        self.assertEqual(tokens["color"]["a9-lime"], "#6DFF30")
        self.assertEqual(tokens["color"]["a9-cyan"], "#29FFE8")
        self.assertEqual(tokens["color"]["a9-navy-900"], "#050E2A")


if __name__ == "__main__":
    unittest.main()

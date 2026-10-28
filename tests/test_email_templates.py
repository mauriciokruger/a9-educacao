"""Contrato do e-mail padrão e da assinatura com foto."""
from html.parser import HTMLParser
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "skills/a9-educacao/assets"


class EmailParts(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []
        self.signatures = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("data-a9-signature") == "true":
            self.signatures += 1
        if tag == "img":
            self.images.append(attrs)


class EmailTemplateContract(unittest.TestCase):
    def test_default_email_and_signature_include_resolvable_photo(self):
        for filename in ("modelo-a9.html", "assinatura-a9.html"):
            with self.subTest(filename=filename):
                path = ASSETS / "emails" / filename
                self.assertTrue(path.is_file(), "Modelo de e-mail ausente")
                parser = EmailParts()
                parser.feed(path.read_text("utf-8"))
                self.assertEqual(parser.signatures, 1, "Assinatura duplicada ou ausente")
                photos = [img for img in parser.images if img.get("data-a9-photo") == "example"]
                self.assertEqual(len(photos), 1, "O padrão precisa incluir o espaço da foto")
                self.assertTrue(photos[0].get("alt"))
                for img in parser.images:
                    target = (path.parent / img["src"]).resolve()
                    self.assertTrue(target.is_relative_to(ASSETS.resolve()))
                    self.assertTrue(target.is_file(), img["src"])


if __name__ == "__main__":
    unittest.main()

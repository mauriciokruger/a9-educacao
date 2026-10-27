"""Conferência opcional de artefato com pypdf e PNGs renderizados pelo Poppler."""
from pathlib import Path
import unittest

try:
    from pypdf import PdfReader
    from PIL import Image
except ImportError:
    PdfReader = Image = None

ROOT = Path(__file__).resolve().parents[1]


@unittest.skipIf(PdfReader is None, "pypdf/Pillow não instalados; teste do pacote continua independente")
class PdfContract(unittest.TestCase):
    def test_all_eight_slides_exist(self):
        reader = PdfReader(ROOT / "docs/demo-a9.pdf")
        self.assertEqual(len(reader.pages), 8)
        self.assertTrue(all(len(page.extract_text()) > 80 for page in reader.pages))
        self.assertTrue(all(abs(float(page.mediabox.width) / float(page.mediabox.height) - 16 / 9) < .001 for page in reader.pages))

    @unittest.skipUnless((ROOT / ".work/slide-1.png").exists(), "PNGs de QA não renderizados")
    def test_cover_background_fills_page(self):
        image = Image.open(ROOT / ".work/slide-1.png").convert("RGB")
        width, height = image.size
        self.assertEqual(image.getpixel((int(width*.96),int(height*.92))), (3,8,28))


if __name__ == "__main__":
    unittest.main()

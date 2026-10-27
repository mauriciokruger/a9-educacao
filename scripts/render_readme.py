"""Exporta arte nativa HTML/CSS do README. Uso editorial opcional: Chrome + Pillow."""
import argparse
import base64
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]


def uri(path, mime):
    return "data:"+mime+";base64,"+base64.b64encode(path.read_bytes()).decode("ascii")


def render(chrome):
    from PIL import Image
    assets = ROOT/"skills/a9-educacao/assets"
    work = ROOT/".work/readme-art"
    work.mkdir(parents=True, exist_ok=True)
    out = ROOT/"docs/assets"
    out.mkdir(parents=True, exist_ok=True)
    fonts = []
    for name, weight in [("Regular",400),("SemiBold",600),("Bold",700)]:
        fonts.append('@font-face{font-family:Poppins;font-style:normal;font-weight:'+str(weight)+';src:url("'+uri(assets/f"fonts/Poppins-{name}.ttf","font/ttf")+'") format("truetype")}')
    html = (ROOT/"scripts/readme-art.html").read_text("utf-8")
    html = html.replace("{{FONT_CSS}}","\n".join(fonts)).replace("{{LOGO}}",uri(assets/"logos/a9-branco.png","image/png"))
    source = work/"art.html"
    source.write_text(html,"utf-8",newline="\n")
    screenshot = work/"art.png"
    before = screenshot.stat().st_mtime_ns if screenshot.exists() else 0
    subprocess.run([str(chrome),"--headless=new","--disable-gpu","--hide-scrollbars","--default-background-color=00000000",
                    "--no-first-run","--no-default-browser-check","--host-resolver-rules=MAP * ~NOTFOUND",
                    "--user-data-dir="+str(work/"profile"),"--force-device-scale-factor=1",
                    "--window-size=1600,776","--screenshot="+str(screenshot),source.as_uri()],
                   check=True,capture_output=True,timeout=45)
    deadline = time.monotonic()+15
    while time.monotonic()<deadline:
        if screenshot.exists() and screenshot.stat().st_mtime_ns>before:
            try:
                with Image.open(screenshot) as image:
                    image.load()
                    image.crop((0,0,1600,620)).save(out/"a9-educacao-capa.png",optimize=True)
                    for name,x in [("baixar-skill",40),("como-instalar",432),("ver-exemplos",824)]:
                        image.crop((x-12,654,x+372,742)).save(out/("botao-"+name+".png"),optimize=True)
                break
            except OSError:
                pass
        time.sleep(.1)
    else:
        raise RuntimeError("Exportação da arte do README não concluiu.")
    print(out)


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chrome",type=Path,required=True)
    render(parser.parse_args().chrome)

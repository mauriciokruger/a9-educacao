"""Constrói os HTMLs offline, tokens CSS e ZIP. Requer somente Python 3.10+."""
import argparse
import base64
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "a9-educacao"
ASSETS = SKILL / "assets"
VERSION = (ROOT / "VERSION").read_text("utf-8").strip()


def data_uri(path, mime):
    return "data:" + mime + ";base64," + base64.b64encode(path.read_bytes()).decode("ascii")


def build():
    tokens = json.loads((ASSETS / "tokens/tokens.json").read_text("utf-8"))
    lines = ["/* Gerado a partir de tokens.json. Fonte de construção no repositório A9 Educação. */", ":root {"]
    for group, values in tokens.items():
        if isinstance(values, dict):
            lines.extend(f"  --{name}: {value};" for name, value in values.items())
    lines.append("}")
    css = "\n".join(lines) + "\n"
    (ASSETS / "tokens/tokens.css").write_text(css, "utf-8", newline="\n")
    font_css = []
    for file, weight in [("Regular", 400), ("Medium", 500), ("SemiBold", 600), ("Bold", 700), ("Black", 900)]:
        uri = data_uri(ASSETS / f"fonts/Poppins-{file}.ttf", "font/ttf")
        font_css.append(f'@font-face{{font-family:"Poppins";font-style:normal;font-weight:{weight};font-display:swap;src:url("{uri}") format("truetype")}}')
    mono = data_uri(ASSETS / "fonts/JetBrainsMono-Variable.ttf", "font/ttf")
    font_css.append(f'@font-face{{font-family:"JetBrains Mono";font-style:normal;font-weight:100 800;font-display:swap;src:url("{mono}") format("truetype")}}')
    source = (ROOT / "scripts/deck.template.html").read_text("utf-8")
    html = source.replace("{{FONT_CSS}}", "\n".join(font_css)).replace("{{TOKENS_CSS}}", css)
    html = html.replace("{{LOGO_WHITE}}", data_uri(ASSETS / "logos/a9-branco.png", "image/png"))
    demo = ASSETS / "apresentacoes/demo-a9.html"
    demo.write_text(html, "utf-8", newline="\n")
    model = html.replace("IA na rotina da equipe", "[Título da apresentação]")
    model = model.replace("Uma tarefa real. Um pedido claro. Uma revisão cuidadosa.", "[Contexto, público e objetivo]")
    model = model.replace("Demonstração do padrão A9", "Modelo editável do padrão A9")
    (ASSETS / "apresentacoes/modelo-a9.html").write_text(model, "utf-8", newline="\n")
    return demo


def validate():
    entry = (SKILL / "SKILL.md").read_text("utf-8")
    front = re.match(r"^---\nname: ([^\n]+)\ndescription: ([^\n]+)\n---", entry)
    if not front or front[1] != SKILL.name or len(front[2]) > 200:
        raise ValueError("Nome/frontmatter inválido ou descrição maior que 200 caracteres.")
    for path in SKILL.rglob("*.md"):
        content = path.read_text("utf-8")
        for link in re.findall(r"\]\(([^)]+)\)", content):
            if "://" in link or link.startswith("#"):
                continue
            target = (path.parent / unquote(link.split("#")[0])).resolve()
            if not target.is_relative_to(SKILL.resolve()) or not target.exists():
                raise ValueError(f"Referência ausente ou fora do pacote em {path.name}: {link}")
        if re.search(r"(?:sk-proj-|ghp_|github_pat_)[A-Za-z0-9_]{15,}", content):
            raise ValueError(f"Possível segredo em {path.name}")
    for name in ("demo-a9.html", "modelo-a9.html"):
        html = (ASSETS / "apresentacoes" / name).read_text("utf-8")
        if "{{" in html or re.search(r'(?:src|href)=["\x27]https?://', html):
            raise ValueError(f"HTML incompleto ou dependente de rede: {name}")
    return True


def package(output):
    build()
    validate()
    output.mkdir(parents=True, exist_ok=True)
    archive = output / f"a9-educacao-v{VERSION}.zip"
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as bundle:
        for path in sorted(SKILL.rglob("*")):
            if path.is_file():
                info = zipfile.ZipInfo("a9-educacao/" + path.relative_to(SKILL).as_posix(), (2026, 10, 27, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.create_system = 3
                info.external_attr = 0o100644 << 16
                bundle.writestr(info, path.read_bytes())
    checksum = hashlib.sha256(archive.read_bytes()).hexdigest()
    (output / "SHA256SUMS.txt").write_text(f"{checksum}  {archive.name}\n", "utf-8", newline="\n")
    return archive


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validar arquivos existentes sem reconstruir")
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    if args.check:
        validate()
        print("Pacote válido.")
    else:
        print(package(args.output))

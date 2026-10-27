"""QA opcional da apresentação em Chrome isolado. Sem perfil ou credenciais do usuário."""
import argparse
from functools import partial
from html import unescape
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import re
import subprocess
import threading
import time

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"


def run(chrome, mode):
    WORK.mkdir(exist_ok=True)
    received = threading.Event()
    reports = []
    class QuietHandler(SimpleHTTPRequestHandler):
        def log_message(self, *args):
            pass
        def do_POST(self):
            if self.path != "/qa-result":
                self.send_error(404)
                return
            reports.append(json.loads(self.rfile.read(int(self.headers["Content-Length"]))))
            self.send_response(200)
            self.end_headers()
            received.set()
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(ROOT)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{server.server_port}"
    command = [str(chrome), "--headless=new", "--disable-gpu", "--no-first-run",
               "--no-default-browser-check", "--no-pdf-header-footer",
               "--force-prefers-reduced-motion=reduce", "--host-resolver-rules=MAP * ~NOTFOUND, EXCLUDE 127.0.0.1",
               "--user-data-dir=" + str(WORK / "chrome-qa")]
    if mode == "pdf":
        command += ["--print-to-pdf="+str(ROOT/"docs/demo-a9.pdf"),
                    base+"/skills/a9-educacao/assets/apresentacoes/demo-a9.html"]
    else:
        command += ["--dump-dom", "--virtual-time-budget=15000", base+"/scripts/qa.html"]
    try:
        before = (ROOT/"docs/demo-a9.pdf").stat().st_mtime_ns if (ROOT/"docs/demo-a9.pdf").exists() else 0
        result = subprocess.run(command, capture_output=True, timeout=60)
        if result.returncode:
            raise RuntimeError("Renderizador retornou erro "+str(result.returncode))
        if mode == "test":
            if not received.wait(30):
                (WORK/"qa-renderer-stderr.txt").write_bytes(result.stderr)
                raise RuntimeError("QA não concluiu em 30s. Consulte .work/qa-renderer-stderr.txt")
            report = reports[0]
            (WORK/"browser-checks.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), "utf-8")
            print(json.dumps(report, ensure_ascii=False, indent=2))
            if not report["passed"]:
                raise SystemExit(1)
        else:
            deadline = time.monotonic()+30
            while time.monotonic()<deadline:
                pdf = ROOT/"docs/demo-a9.pdf"
                if pdf.exists() and pdf.stat().st_mtime_ns > before and pdf.stat().st_size > 10000:
                    break
                time.sleep(.1)
            else:
                raise RuntimeError("Exportação PDF não concluiu em 30s.")
            print(ROOT/"docs/demo-a9.pdf")
    finally:
        server.shutdown()
        server.server_close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chrome", type=Path, required=True)
    parser.add_argument("--mode", choices=["test", "pdf"], default="test")
    options = parser.parse_args()
    run(options.chrome, options.mode)

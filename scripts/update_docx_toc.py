from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import uno
from com.sun.star.beans import PropertyValue


def prop(name: str, value):
    item = PropertyValue()
    item.Name = name
    item.Value = value
    return item


def connect(port: int, attempts: int = 30):
    local_ctx = uno.getComponentContext()
    resolver = local_ctx.ServiceManager.createInstanceWithContext(
        "com.sun.star.bridge.UnoUrlResolver", local_ctx
    )
    url = f"uno:socket,host=127.0.0.1,port={port};urp;StarOffice.ComponentContext"
    last_error = None
    for _ in range(attempts):
        try:
            return resolver.resolve(url)
        except Exception as exc:
            last_error = exc
            time.sleep(0.5)
    raise RuntimeError(f"Could not connect to LibreOffice: {last_error}")


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: update_docx_toc.py <document.docx>")

    path = Path(sys.argv[1]).resolve()
    if not path.exists():
        raise SystemExit(f"File not found: {path}")

    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice:
        raise SystemExit("LibreOffice is required to materialize the table of contents")

    port = 2083
    with tempfile.TemporaryDirectory(prefix="normalfall-lo-") as tmp:
        tmp_path = Path(tmp)
        profile = tmp_path / "profile"
        home = tmp_path / "home"
        profile.mkdir()
        home.mkdir()
        env = os.environ.copy()
        env["HOME"] = str(home)
        proc = subprocess.Popen(
            [
                soffice,
                f"-env:UserInstallation=file://{profile}",
                "--headless",
                f"--accept=socket,host=127.0.0.1,port={port};urp;StarOffice.ServiceManager",
                "--norestore",
                "--nodefault",
                "--nofirststartwizard",
            ],
            env=env,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        try:
            ctx = connect(port)
            desktop = ctx.ServiceManager.createInstanceWithContext(
                "com.sun.star.frame.Desktop", ctx
            )
            doc = desktop.loadComponentFromURL(
                uno.systemPathToFileUrl(str(path)),
                "_blank",
                0,
                (prop("Hidden", True),),
            )
            if doc is None:
                raise RuntimeError(f"LibreOffice could not open {path}")

            indexes = doc.getDocumentIndexes()
            index_count = indexes.getCount()
            if index_count < 1:
                raise RuntimeError("No table of contents/index found in DOCX")
            for i in range(index_count):
                indexes.getByIndex(i).update()

            doc.store()
            doc.close(True)
            print(f"Updated {index_count} document index(es) in {path}")
        finally:
            proc.terminate()
            try:
                proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                proc.kill()


if __name__ == "__main__":
    main()

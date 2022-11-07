from pathlib import Path
from typing import Optional

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


def _get_static_directory() -> str:
    return str(Path(__file__).parent.parent.joinpath("static").resolve())


def _get_templates_directory() -> str:
    return str(Path(__file__).parent.parent.joinpath("templates").resolve())


def mount_static(
    app: FastAPI,
    static_url: Optional[str] = "/static",
    directory: Optional[str] = None,
    name: Optional[str] = "static",
) -> None:
    if directory is None:
        directory = _get_static_directory()

    app.mount(path=static_url, app=StaticFiles(directory=directory), name=name)


templates = Jinja2Templates(directory=_get_templates_directory())

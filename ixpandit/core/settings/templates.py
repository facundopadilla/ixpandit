from typing import Optional

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


def mount_static(
        app: FastAPI,
        static_url: Optional[str] = "/static",
        directory: Optional[str] = "ixpandit/core/static",
        name: Optional[str] = "static"
) -> None:
    app.mount(
        path=static_url,
        app=StaticFiles(directory=directory),
        name=name
    )


templates = Jinja2Templates(directory="ixpandit/core/templates")

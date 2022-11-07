from fastapi import FastAPI

from ixpandit.core.settings.templates import mount_static
from ixpandit.routers import base_router

app = FastAPI()
mount_static(app=app)
app.include_router(router=base_router)

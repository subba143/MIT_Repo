from fastapi import FastAPI
from .routers import report

app = FastAPI()

app.include_router(report.router, prefix="/api")

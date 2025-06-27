from fastapi import FastAPI
from backend.routes.dashboard import router as dashboard_router

app = FastAPI(title="Crypto Dashboard API")


app.include_router(dashboard_router)


from fastapi import FastAPI
from backend.routes.dashboard import router as dashboard_router
from backend.routes.portfolio import router as portfolio_router

app = FastAPI(title="Crypto Dashboard API")


app.include_router(dashboard_router)
app.include_router(portfolio_router)


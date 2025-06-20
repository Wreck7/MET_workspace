from fastapi import FastAPI
from controller import router as urls_router

app = FastAPI()

app.include_router(urls_router)






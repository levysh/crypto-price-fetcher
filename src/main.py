from fastapi import APIRouter, FastAPI

from src.config import settings
from src.currency.router import api_router as currency_router
from src.database import init_db

app = FastAPI(
    title=settings.PROJECT_NAME,
)

api_router = APIRouter()
api_router.include_router(currency_router, prefix="/prices", tags=["prices"])
app.include_router(api_router, prefix=settings.API_PREFIX)


@app.on_event("startup")
def on_startup():
    init_db()

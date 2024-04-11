from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload

from src.currency.models import Currency
from src.currency.schemas import CurrencySchema
from src.database import get_db

api_router = APIRouter()


@api_router.get("/", response_model=List[CurrencySchema])
def list_prices(session: Session = Depends(get_db)) -> Any:
    """
    Retrieve items.
    """

    return session.query(Currency).options(joinedload(Currency.prices)).all()


@api_router.get(
    "/{name}", response_model=CurrencySchema, responses={404: {"description": "Item not found"}}
)
def get_price(name: str, session: Session = Depends(get_db)) -> Any:
    """
    Get item by ID.
    """
    currency = (
        session.query(Currency)
        .filter(Currency.name == name)
        .options(joinedload(Currency.prices))
        .first()
    )
    if currency is None:
        raise HTTPException(status_code=404, detail="Currency not found")

    return currency

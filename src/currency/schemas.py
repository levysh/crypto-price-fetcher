from datetime import datetime
from typing import List

from pydantic import BaseModel

from src.currency.models import CurrencyPriceProvider


class CurrencyPriceSchema(BaseModel):
    received_at: datetime
    price: float
    price_provider: CurrencyPriceProvider


class CurrencySchema(BaseModel):
    name: str
    prices: List[CurrencyPriceSchema]

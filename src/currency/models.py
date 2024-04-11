import datetime as dt
from enum import Enum

from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.currency.crypto_providers_clients import BinanceClient, ByBitClient
from src.database import Base


class CurrencyPriceProvider(str, Enum):
    BINANCE = "binance"
    BYBIT = "bybit"


class CurrencyProviderClientFactory:
    _providers = {
        CurrencyPriceProvider.BINANCE: BinanceClient,
        CurrencyPriceProvider.BYBIT: ByBitClient,
    }

    @classmethod
    def get_provider(cls, provider_enum):
        provider_class = cls._providers.get(provider_enum)
        if not provider_class:
            raise ValueError(f"Provider for {provider_enum} not supported")
        return provider_class()


class Currency(Base):
    __tablename__ = "currency"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    name: Mapped[str] = mapped_column(unique=True)
    send_name: Mapped[str] = mapped_column(unique=True)


class CurrencyPrice(Base):
    __tablename__ = "currency_price"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    received_at: Mapped[dt.datetime] = mapped_column(default=dt.datetime.now)
    price: Mapped[float]
    price_provider: Mapped[CurrencyPriceProvider]
    currency_id = Column(Integer, ForeignKey("currency.id", ondelete="CASCADE"))
    currency = relationship("Currency", backref="prices")

    # store only latest value for each pair price_provider + currency
    __table_args__ = (
        UniqueConstraint("currency_id", "price_provider", name="_currency_provider_uc"),
    )

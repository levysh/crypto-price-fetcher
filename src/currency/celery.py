from src.celery_app import app
from src.database import SessionLocal


@app.task
def fetch_prices_impl(provider):
    from datetime import datetime

    from sqlalchemy import and_

    from src.currency.models import (
        Currency,
        CurrencyPrice,
        CurrencyProviderClientFactory,
    )

    client = CurrencyProviderClientFactory.get_provider(provider)

    session = SessionLocal()
    currencies_map = {currency.send_name: currency for currency in session.query(Currency).all()}

    prices_map = client.get_prices(currencies_map.keys())
    received_at = datetime.now()

    for name, price in prices_map.items():
        currency = currencies_map.get(name)
        if currency:
            existing_price = (
                session.query(CurrencyPrice)
                .filter(
                    and_(
                        CurrencyPrice.currency_id == currency.id,
                        CurrencyPrice.price_provider == provider,
                    )
                )
                .one_or_none()
            )

            if existing_price:
                existing_price.price = price
                existing_price.received_at = received_at
            else:
                new_price = CurrencyPrice(
                    received_at=received_at,
                    price=price,
                    price_provider=provider,
                    currency_id=currency.id,
                )
                session.add(new_price)

    session.commit()
    session.close()


@app.task
def fetch_prices():
    from src.currency.models import CurrencyPriceProvider

    for provider in CurrencyPriceProvider:
        fetch_prices_impl.delay(provider)


app.conf.beat_schedule.update(
    {
        "fetch-prices-each-30-secs": {
            "task": "src.currency.celery.fetch_prices",
            "schedule": 30.0,
        },
    }
)

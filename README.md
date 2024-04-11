# Crypto price fetcher README

## Completion Note

I finished the task, but there wasn't a lot of time. Because of this, there are some parts that still need work, especially **tests**.

### Changes Made

I changed the data format to make the code better in three ways:

1. **Make the code more solid and organized**.
2. **Improve how the system handles different kinds of data and make it easy to update**.
3. **Add timestamps so users know how fresh or old the data is**.

Here's what the new data looks like:

```json
[
  {
    "name": "BTC",
    "prices": [
      {
        "received_at": "2024-04-11T00:14:17.251470",
        "price": 70463.67,
        "price_provider": "binance"
      },
      {
        "received_at": "2024-04-11T00:14:17.432419",
        "price": 70501.5,
        "price_provider": "bybit"
      }
    ]
  },
  {
    "name": "ETH",
    "prices": [
      {
        "received_at": "2024-04-11T00:14:17.251470",
        "price": 3533.18,
        "price_provider": "binance"
      },
      {
        "received_at": "2024-04-11T00:14:17.432419",
        "price": 3534.72,
        "price_provider": "bybit"
      }
    ]
  }
]
```

### TODOs

**Must-haves:**
- Add tests.
- Rethink the data model (maybe keep a history instead of overwriting?).
- Implement logging and alerts.
- Decide on fetch frequency and add caching.
- Set up alembic for database migrations.

**Nice-to-haves:**
- Switch to pipenv or poetry instead of requirements.
- Add type annotations everywhere.
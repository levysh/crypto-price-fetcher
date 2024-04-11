from typing import Dict, List

from pydantic import HttpUrl

from .base_client import BaseCryptoClient


class BinanceClient(BaseCryptoClient):
    @property
    def data_endpoint(self) -> HttpUrl:
        return "https://api.binance.com/api/v3/ticker/price"

    def _response_json_to_dict(self, response_json: Dict, symbols: List[str]) -> Dict[str, float]:
        return {
            item["symbol"]: item["price"] for item in response_json if item["symbol"] in symbols
        }

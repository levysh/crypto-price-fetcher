from typing import Dict, List

from pydantic import HttpUrl

from .base_client import BaseCryptoClient


class ByBitClient(BaseCryptoClient):
    @property
    def data_endpoint(self) -> HttpUrl:
        return "https://api.bybit.com/v2/public/tickers"

    def _response_json_to_dict(self, response_json: Dict, symbols: List[str]) -> Dict[str, float]:
        return {
            item["symbol"]: item["last_price"]
            for item in response_json["result"]
            if item["symbol"] in symbols
        }

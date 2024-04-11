from .base_client import BaseCryptoClient


class BinanceClient(BaseCryptoClient):
    DATA_ENDPOINT = "https://api.binance.com/api/v3/ticker/price"

    def _response_json_to_dict(self, response_json, symbols):
        return {
            item["symbol"]: item["price"] for item in response_json if item["symbol"] in symbols
        }

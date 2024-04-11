from .base_client import BaseCryptoClient


class ByBitClient(BaseCryptoClient):
    DATA_ENDPOINT = "https://api.bybit.com/v2/public/tickers"

    def _response_json_to_dict(self, response_json, symbols):
        return {
            item["symbol"]: item["last_price"]
            for item in response_json["result"]
            if item["symbol"] in symbols
        }

from abc import ABC, abstractmethod

import requests
from retry import retry


class BaseCryptoClient(ABC):
    DATA_ENDPOINT = None

    @abstractmethod
    def _response_json_to_dict(self, response_json, symbols):
        pass

    # TODO: find a way to retrieve only requested symbols
    @retry(requests.exceptions.RequestException, tries=4, delay=2, backoff=2)
    def _get_raw_prices_data(self):
        response = requests.get(self.DATA_ENDPOINT)
        response.raise_for_status()
        return response.json()

    def get_prices(self, symbols):
        # TODO: validate that all symbols are in the result
        response_json = self._get_raw_prices_data()
        return self._response_json_to_dict(response_json, symbols)

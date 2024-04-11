from abc import ABC, abstractmethod
from typing import Dict, List

import requests
from pydantic import HttpUrl
from retry import retry


class BaseCryptoClient(ABC):
    @property
    @abstractmethod
    def data_endpoint(self) -> HttpUrl:
        pass

    @abstractmethod
    def _response_json_to_dict(self, response_json: Dict, symbols: List[str]) -> Dict[str, float]:
        pass

    # TODO: find a way to retrieve only requested symbols
    @retry(requests.exceptions.RequestException, tries=4, delay=2, backoff=2)
    def _get_raw_prices_data(self) -> dict:
        response = requests.get(self.data_endpoint)
        response.raise_for_status()
        return response.json()

    def get_prices(self, symbols: List[str]) -> Dict[str, float]:
        # TODO: validate that all symbols are in the result
        response_json = self._get_raw_prices_data()
        return self._response_json_to_dict(response_json, symbols)

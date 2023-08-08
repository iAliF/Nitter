from abc import abstractmethod
from typing import Dict, Any, List

import requests
from requests import RequestException

from ..models import MediaResult


class SourceBase:
    def __init__(self, source_name: str, base_url: str, timeout=10, proxies=None) -> None:
        self.source_name = source_name
        self.timeout = timeout
        self.proxies = proxies

        self._session = requests.Session()
        self._base_url = base_url

    @abstractmethod
    def get_medias(self, username: str) -> List[MediaResult]:
        pass

    def _make_request(self, path: str, params: Dict[str, Any] = None) -> str:
        try:
            req = self._session.get(
                f"{self._base_url}/{path}",
                params=params,
                timeout=self.timeout,
                proxies=self.proxies
            )
            return req.text
        except RequestException as e:
            print(e)

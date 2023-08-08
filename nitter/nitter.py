import time
from datetime import datetime
from typing import List, Dict, Any
from xml.etree import ElementTree

from bs4 import BeautifulSoup
from requests import HTTPError, ConnectionError, Session

from .exceptions import NetworkException
from .models import MediaResult


class Nitter:
    def __init__(self, timeout=10, proxies=None) -> None:
        self.timeout = timeout

        self._session = Session()
        self._session.proxies = proxies

        self._base_url = 'https://nitter.moomoo.me'

    def get_media(self, username: str) -> List[MediaResult]:
        media = []

        data = self._make_request(f"{username}/media/rss")
        root = ElementTree.fromstring(data)

        for item in root.findall('channel/item'):
            bs4 = BeautifulSoup(
                item.find('description').text,
                'html.parser'
            )

            caption = bs4.find('p').text or None
            images = [
                img['src']
                for img in bs4.find_all('img')
            ]
            dt = datetime.fromtimestamp(
                time.mktime(
                    time.strptime(
                        item.find('pubDate').text,
                        '%a, %d %b %Y %H:%M:%S GMT'
                    )
                )
            )

            media.append(
                MediaResult(
                    caption,
                    images,
                    dt
                )
            )

        return media

    def _make_request(self, path: str, params: Dict[str, Any] = None) -> str:
        try:
            req = self._session.get(
                f"{self._base_url}/{path}",
                params=params,
                timeout=self.timeout,
            )
            return req.text
        except (ConnectionError, HTTPError):
            raise NetworkException(f"Cannot connect to Nitter")

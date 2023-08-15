import time
from datetime import datetime
from typing import List, Dict, Any

from bs4 import BeautifulSoup
from requests import HTTPError, ConnectionError, Session

from .exceptions import NetworkException
from .models import MediaResult, Image


class Nitter:
    def __init__(self, timeout=10, proxies=None) -> None:
        self.timeout = timeout

        self._session = Session()
        self._session.proxies = proxies

        self._base_url = 'https://nitter.moomoo.me'

    def format_url(self, url: str) -> str:
        return f'{self._base_url}{url}'

    def get_media(self, username: str) -> List[MediaResult]:
        media = []

        data = self._make_request(f"{username}/media")
        bs4 = BeautifulSoup(
            data,
            'html.parser'
        )

        for item in bs4.find_all('div', {'class': 'timeline-item'}):
            caption = item.find_next('div', {'class': 'tweet-content media-body'}).text

            tweet_date = item.find_next('span', {'class': 'tweet-date'})
            tweet_date = datetime.fromtimestamp(
                time.mktime(
                    time.strptime(
                        tweet_date.find('a')["title"],
                        '%b %d, %Y · %H:%M %p UTC'
                    )
                )
            )

            images = []
            for image in item.find_all('div', {'class': 'attachment image'}):
                images.append(
                    Image(
                        self.format_url(image.find_next('a', {'class': 'still-image'})['href'])
                    )
                )

            media.append(
                MediaResult(
                    caption,
                    images,
                    tweet_date
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

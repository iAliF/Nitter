from typing import List
from xml.etree import ElementTree

from bs4 import BeautifulSoup

from .base import SourceBase
from ..models import MediaResult


class Nitter(SourceBase):
    def __init__(self) -> None:
        super().__init__(
            'Nitter',
            'https://nitter.moomoo.me'
        )

    def get_medias(self, username: str) -> List[MediaResult]:
        medias = []

        data = self._make_request(f"{username}/media/rss")
        root = ElementTree.fromstring(data)

        for item in root.findall('channel/item/description'):
            bs4 = BeautifulSoup(item.text, 'html.parser')

            caption = bs4.find('p').text or None
            images = [
                img['src']
                for img in bs4.find_all('img')
            ]

            medias.append(
                MediaResult(
                    caption,
                    images
                )
            )

        return medias

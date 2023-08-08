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

    def get_medias(self, username: str) -> MediaResult:
        images = []

        data = self._make_request(f"{username}/media")
        print(data)
        root = ElementTree.fromstring(data)

        for item in root.findall('channel/item/description'):
            print(item, end="=============\n")



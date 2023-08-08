from abc import abstractmethod

from ..models import MediaResult


class SourceBase:
    def __init__(self, source_name: str, base_url: str) -> None:
        self.source_name = source_name
        self._base_url = base_url

    @abstractmethod
    def get_medias(self) -> MediaResult:
        pass

from dataclasses import dataclass
from typing import List


@dataclass
class Image:
    src: str


@dataclass
class MediaResult:
    images: List[Image]

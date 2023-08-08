from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Image:
    src: str


@dataclass
class MediaResult:
    caption: Optional[str]
    images: List[Image]

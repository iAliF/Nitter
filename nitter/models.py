from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional


@dataclass
class Image:
    src: str

    def __str__(self) -> str:
        return self.src

    def __repr__(self) -> str:
        return f"Image({self.src})"


@dataclass
class MediaResult:
    caption: Optional[str]
    images: List[Image]
    pub_date: datetime

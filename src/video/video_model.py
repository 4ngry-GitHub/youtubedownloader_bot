from typing import Union, Optional

from dataclasses import dataclass


@dataclass
class VideoModel:
    path: str
    title: str
    description: str
    performer: Optional[str]
    thumb: Union[str, bytes]
    
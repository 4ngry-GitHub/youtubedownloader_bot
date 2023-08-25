from typing import Union, Optional

from dataclasses import dataclass


@dataclass
class AudioModel:
    path: str
    title: str
    performer: Optional[str]
    thumb: Union[str, bytes]
    
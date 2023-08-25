from dataclasses import dataclass


@dataclass
class VideoConfig:
    resolution: str
    quality: str
    bitrate: int = 44100
    
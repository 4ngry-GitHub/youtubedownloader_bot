from dataclasses import dataclass


@dataclass
class AudioConfig:
    maximum_download_size: float = 23.0
    maximum_convert_size: int = 47280288
    bitrate: int = 44100
    frequency: int = 120


audio_config = AudioConfig()
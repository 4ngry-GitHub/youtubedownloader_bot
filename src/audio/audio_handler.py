import os

from asgiref.sync import sync_to_async
from banditsdk.common.result import Result
from moviepy.editor import AudioFileClip
from pytube import YouTube

from audio.audio_model import AudioModel
from audio.audio_config import audio_config as cfg
from common.log_helper import get_logger


async def download_audio(url: str, logger = get_logger()) -> Result:
    try:
        youtube_audio = YouTube(url)
        youtube_audio = youtube_audio.streams.filter(only_audio=True).first()
        if youtube_audio.filesize_mb > cfg.maximum_download_size:
            return Result.failure("File is too large.")
        await sync_to_async(youtube_audio.download)(output_path="./static/")
    except Exception as error:
        logger.error(str(error))
        return Result.failure(error=str(error))
    return Result.success(youtube_audio.title)


async def convert_audio_file(audio_title: str, logger = get_logger()) -> Result:
    try:
        audio_file = AudioFileClip(f"./static/{audio_title}.mp4")
        await sync_to_async(audio_file.write_audiofile)(f"./static/{audio_title}.mp3")
    except Exception as error:
        logger.error(str(error))
        return Result.failure(error=str(error))
    finally:
        audio_file.close()
    os.remove(f"./static/{audio_title}.mp4")
    if os.path.getsize(f"./static/{audio_title}.mp3") > cfg.maximum_convert_size:
        return Result.failure("File is too large.")
    return Result.success(AudioModel(
                                    path=f"./static/{audio_title}.mp3",
                                    title=audio_title,
                                    performer=None,
                                    thumb=None))

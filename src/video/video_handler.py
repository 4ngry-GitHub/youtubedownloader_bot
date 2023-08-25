import os

from asgiref.sync import sync_to_async
from banditsdk.common.result import Result
from moviepy.editor import VideoFileClip
from pytube import YouTube

from common.log_helper import get_logger
#TODO: refactor.


async def download_video(url: str, logger = get_logger()) -> Result:
    try:
        youtube_video = YouTube(url)
        youtube_video = youtube_video.streams.get_lowest_resolution()
        await sync_to_async(youtube_video.download)(output_path="./static/")
    except Exception as error:
        logger.error(str(error))
        return Result.failure(error=str(error))
    return Result.success(youtube_video.title)


async def convert_video_to_audio(video_file: str, logger = get_logger()) -> Result:
    try:
        video = VideoFileClip(f"./static/{video_file}.mp4")
        await sync_to_async(video.audio.write_audiofile)(f"./static/{video_file}.mp3")
    except Exception as error:
        logger.error(str(error))
        return Result.failure(error=str(error))
    finally:
        video.close()
    os.remove(f"./static/{video_file}.mp4")
    with open(f"./static/{video_file}.mp3", "rb") as file:
        return Result.success(file)
    
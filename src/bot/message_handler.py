import os

from aiogram import types

from audio.audio_handler import download_audio, convert_audio_file
from bot.bot import dp
from common.dependencies import is_valid_link


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message) -> None:
    welcome_text: str = """<b>Hello, friend! Welcome to the YouTube Music Download Bot.
Get ready to groove to your favorite tunes anytime, anywhere.
Our bot is here to help you download those catchy melodies and playlists from YouTube, so you can enjoy them offline.
Whether it's a chart-topper or a hidden gem, you're just a download away from your own music paradise.
Let's start filling your playlist with awesome tracks! 🎶🤖</b>"""
    await message.reply(welcome_text, parse_mode="HTML")


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message) -> None:
    welcome_text: str = """<b>Howdy again, partner! In our help section, we want to make things crystal clear for you.
Here's the scoop: Just paste those YouTube links, and like magic, you'll get back shiny .mp3 files that you can enjoy wherever you go.
No fuss, no hassle – just pure music goodness at your fingertips.
So, let's start turning those links into toe-tappin' tunes! 🎶🤠</b>"""
    await message.reply(welcome_text, parse_mode="HTML")


@dp.message_handler()
async def download_video(message: types.Message) -> None:
    if is_valid_link(message.text).is_failure():
        await message.reply("""Seems like this song is unavailable for bot.
Most likely there is incorrect link or regional restrictions.⛔👷‍♂️""")
        return
    downloading_msg = await message.reply("<b>Fetching the video file for you.☺️⬇️</b>", parse_mode="HTML")
    downloaded_file = await download_audio(message.text)
    if downloaded_file.is_failure():
        await message.reply("Cannot download video. Try again later.🚧😓")
        return
    await downloading_msg.delete()
    converting_msg = await message.reply("<b>Transforming video into audio. We're nearly finished.😊🔄</b>", parse_mode="HTML")
    converted_file = await convert_audio_file(downloaded_file.data)
    if converted_file.is_failure():
        await message.reply("Cannot process video. Try again later.🚧😓")
    await converting_msg.delete()
    with open(converted_file.data.path, mode="rb") as file_to_send:
        binary_file = file_to_send.read()
    await message.reply_audio(binary_file,
                              caption=f'[ <a href="{message.text}">Source</a> ]',
                              title=converted_file.data.title,
                              thumb=converted_file.data.thumb,
                              performer=converted_file.data.performer,
                              parse_mode="HTML")
    os.remove(converted_file.data.path)

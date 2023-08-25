import re

from aiogram import types
from banditsdk.common.result import Result


def get_user_id(message: types.Message) -> int:
    """Method retrieves user_id from a message object.

    Args:
        message (types.Message): aiogram types message object.

    Returns:
        int: user_id or -1 in case of failure.
    """
    if not isinstance(message, types.Message):
        return -1
    return message.chat.id


def is_valid_link(link: str) -> Result:
    # https://youtu.be/
    pattern_short: str = r'^https:\/\/youtu\.be\/.*'
    # https://www.youtube.com/
    pattern_long: str = r"^https:\/\/www\.youtube\.com\/.*"
    is_short = re.match(pattern_short, link)
    if is_short:
        return Result.success()
    is_long = re.match(pattern_long, link)
    if is_long:
        return Result.success()
    return Result.failure(error="Incorrect link.")

from aiogram import executor

from common.log_helper import get_logger
from bot.message_handler import dp
# from settings import settings


def run_bot(logger = get_logger()) -> None:
    logger.info("[+] Bot has been started.")
    executor.start_polling(dispatcher=dp)
    logger.info("[+] Bot has gone offline.")


if __name__ == "__main__":
    run_bot()
    
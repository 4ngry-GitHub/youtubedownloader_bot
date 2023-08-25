from aiogram import Bot, Dispatcher, types

from settings import settings

bot = Bot(settings.telegram_token)
dp = Dispatcher(bot)

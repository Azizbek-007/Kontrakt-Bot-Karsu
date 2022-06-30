from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API_TOKEN = '5483573275:AAH_a22YuTnmYgQ0lQomP1nSp5XLpwG2bj8'
bot_id = API_TOKEN.split(':')[0]
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
admins = [659692188, 1146006872]
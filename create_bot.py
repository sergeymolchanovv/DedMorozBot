from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()  # Хранение данных
TOKEN = ''
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)  # Инициализация бота
dp = Dispatcher(bot, storage=storage)  # Диспэтчер

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.config_dm import TOKEN


storage = MemoryStorage()  # Хранение данных
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)  # Инициализация бота
dp = Dispatcher(bot, storage=storage)  # Диспэтчер

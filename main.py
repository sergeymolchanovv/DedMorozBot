from aiogram import executor
from create_bot import dp
from register_handlers import register_handlers


if __name__ == '__main__':
    register_handlers(dp)
    executor.start_polling(dp, skip_updates=True)

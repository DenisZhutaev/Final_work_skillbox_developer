from aiogram import executor
from telegram import dp

if __name__ == '__main__':
    """
    Функция, запускающая бота

    Параметры:
        - dp: Dispatcher объект из aiogram, отвечающий за обработку обновлений.
    """
    executor.start_polling(dp)

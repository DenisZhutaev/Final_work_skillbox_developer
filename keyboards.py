from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def forecast_buttons(city):
    """
    Функция создает клавиатуру с кнопками для выбора прогноза погоды.

    Параметры:
        :param city: Название города, для которого нужно получить прогноз погоды, str.

    Возвращаемое значение:
        :return: InlineKeyboardMarkup Клавиатура с кнопками для выбора прогноза погоды.
    """
    keyboard = InlineKeyboardMarkup()
    keyboard.row(
        InlineKeyboardButton("Сегодня", callback_data=f"today:{city}"),
        InlineKeyboardButton("Завтра", callback_data=f"tomorrow:{city}"),
    )
    keyboard.add(
        InlineKeyboardButton("Неделя", callback_data=f"week:{city}"),
        InlineKeyboardButton("История", callback_data="history"),
    )

    return keyboard


def help_button():
    """
    Функция создает клавиатуру с кнопкой для вызова помощи.

    Возвращаемое значение:
        :return: InlineKeyboardMarkup Клавиатура с кнопкой для вызова помощи.
    """
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton("Помощь", callback_data="help")
    )

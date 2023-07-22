from datetime import datetime

user_history = {}


def add_to_history(user_id, city):
    """
     Функция добавляет запись о запросе пользователя в историю.

    Параметры:
        :param user_id: идентификатор пользователя, str
        :param city: название города, str

    Возвращаемое значение:
        нет
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if user_id not in user_history:
        user_history[user_id] = []
    user_history[user_id].append((city, timestamp))


def get_history(user_id):
    """
    Параметры:
    :param user_id: идентификатор пользователя, str

    Возвращаемое значение:
        Строка, содержащая историю запросов пользователя в формате:
        "timestamp: city\n"
        Если история пуста, возвращается строка "История пуста."
    """
    if user_id not in user_history or not user_history[user_id]:
        history_text = "История пуста."
    else:
        history_text = "История запросов:\n"
        for city, timestamp in user_history[user_id]:
            history_text += f"{timestamp}: {city}\n"

    return history_text

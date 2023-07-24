import geonamescache
from aiohttp import ClientSession
from datetime import datetime, timedelta


from config import OPENWEATHERMAP_API_KEY


async def request_weather_data(endpoint, **params):
    """
    Асинхронная функция для отправки запроса на API OpenWeatherMap и получения данных о погоде.

    Параметры:
        :param endpoint:  Конечная точка API OpenWeatherMap, str.
        :param params: Параметры запроса, dict.

    Возвращаемое значение:
        :return: Данные о погоде или прогнозе погоды или None, если запрос не был успешным, dict.
    """
    params.update({'appid': OPENWEATHERMAP_API_KEY,
                   'units': 'metric', 'lang': 'ru'})
    url = f"http://api.openweathermap.org/data/2.5/{endpoint}"

    async with ClientSession() as session:
        async with session.get(url, params=params) as response:
            data = await response.json()
            if data.get('cod') != 200 and data.get('cod') != "200":
                return None
            return data


async def get_weather(city: str = None, lat: float = None, lon: float = None):
    """
    Функция для получения данных о погоде для заданного города или координат.

    Параметры:
        :param city: Название города, str.
        :param lat: Широта, float.
        :param lon: Долгота, float.

    Возвращаемое значение:
        :return: Данные о погоде или None, если не указаны город или координаты, dict.
    """
    params = {}
    if city:
        params['q'] = city
    elif lat is not None and lon is not None:
        params['lat'] = lat
        params['lon'] = lon
    else:
        return None

    return await request_weather_data("weather", **params)


async def get_forecast(city: str, days: int = 1):
    """
    Функция для получения прогноза погоды на указанное количество дней для заданного города.

    Параметры:
        :param city: Название города, str.
        :param days: Количество дней прогноза (по умолчанию 1), int.

    Возвращаемое значение:
        :return: Данные о прогнозе погоды, dict.
    """
    params = {'q': city}
    return await request_weather_data("forecast", **params)


def get_weather_icon(weather_id):
    """
    Функция для получения символа погоды на основе идентификатора погоды.

    Параметры:
        :param weather_id: Идентификатор погоды, int.

    Возвращаемое значение:
        :return: Символ погоды, str.
    """
    if 200 <= weather_id <= 232:
        return "⛈️"  # Гроза
    elif 300 <= weather_id <= 531:
        return "🌧️"  # Дождь
    elif 600 <= weather_id <= 622:
        return "❄️"  # Снег
    elif 800 == weather_id:
        return "☀️"  # Ясно
    else:
        return "☁️"  # Облачно


def format_weather(data):
    """
    Функция для форматирования данных о погоде в строку.

    Параметры:
        :param data:  Данные о погоде.

    Возвращаемое значение:
        :return: Строка с форматированными данными о погоде, str.
    """
    city = data['name']
    temp = round(data['main']['temp'])  # Округление температуры до целых
    feels_like = round(data['main']['feels_like'])
    description = data['weather'][0]['description']
    weather_id = data['weather'][0]['id']

    sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M')
    sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M')
    day_duration = timedelta(seconds=data['sys']['sunset'] -
                                     data['sys']['sunrise'])
    day_duration_str = (f"{day_duration.seconds // 3600} ч "
                        f"{day_duration.seconds % 3600 // 60} мин")

    weather_icon = get_weather_icon(weather_id)

    weather_str = (f"{city}:\n{weather_icon} Температура: {temp}°C\n"
                   f"Ощущается как: {feels_like}"
                   f"°C\n{description.capitalize()}\n"
                   f"Восход солнца: {sunrise}\nЗакат солнца: {sunset}\n"
                   f"Продолжительность дня: {day_duration_str}\n"
                   f"Хорошего дня! 🙂")

    return weather_str


def format_forecast(data, days=1):
    """
    Функция для форматирования данных о прогнозе погоды в строку.

    Параметры:
        :param data: Данные о прогнозе погоды.
        :param days: Количество дней прогноза (по умолчанию 1), int.

    Возвращаемое значение:
        :return: Строка с форматированными данными о прогнозе погоды, str.
    """
    city = data['city']['name']
    weather_list = data['list']
    country = data['city']['country']
    country = get_country_name(country)

    if days == 1:
        period = "сегодня"
    elif days == 2:
        period = "завтра"
    else:
        period = f"следующие {days} дней"

    forecast_str = f"Прогноз погоды в {city}, {country} на {period}:\n"

    city_sunrise = datetime.fromtimestamp(
        data['city']['sunrise']).strftime('%H:%M')
    city_sunset = datetime.fromtimestamp(
        data['city']['sunset']).strftime('%H:%M')
    city_day_duration = timedelta(
        seconds=data['city']['sunset'] - data['city']['sunrise'])
    city_day_duration_str = f"{city_day_duration.seconds // 3600} ч " \
                            f"{city_day_duration.seconds % 3600 // 60} мин"

    for i, weather_data in enumerate(weather_list[::8][:days]):
        date = weather_data['dt_txt'][:10]
        temp = round(weather_data['main']['temp'])
        description = weather_data['weather'][0]['description']
        weather_id = weather_data['weather'][0]['id']

        weather_icon = get_weather_icon(weather_id)

        forecast_str += (f"{date}: {weather_icon} Температура: {temp}°C, "
                         f"{description.capitalize()}"
                         f"\nВосход солнца: {city_sunrise}\n"
                         f"Закат солнца: {city_sunset}\n"
                         f"Продолжительность дня: {city_day_duration_str}\n"
                         f"Хорошего дня! 🙂\n\n")

    return forecast_str


def get_country_name(country_code):
    gc = geonamescache.GeonamesCache()
    countries = gc.get_countries()

    if country_code in countries:
        country_name = countries[country_code]['name']
        return country_name

    return None

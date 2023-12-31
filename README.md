>## Добро пожаловать в мир удивительного и функционального Telegram-бота погоды WeatherNow! 

![d1536634.png](d1536634.png)

С этим ботом вы всегда будете в курсе актуальной погоды, будь то солнечный летний день или холодное зимнее утро. 

Наш бот [@OpenWatherNowBot](https://t.me/OpenWatherNowBot) создан с одной целью — облегчить вашу жизнь и помочь 
вам планировать свой день. Подключитесь к нашему боту, и вы сможете получать свежие данные о погоде в любом месте 
и в любое время. Никогда раньше получение прогноза погоды не было таким простым и удобным!

Что же делает нашего бота погоды настолько привлекательным и незаменимым? Во-первых, он обладает высочайшей 
точностью прогноза. Мы сотрудничаем с ведущими метеорологическими службами и поставщиками данных, чтобы 
предоставлять вам только самую актуальную и достоверную информацию. Наш бот учитывает все факторы – температуру, 
восход солнца, закат солнца, продолжительность дня. Вы будете знать, как одеться, чтобы 
чувствовать себя комфортно в любую погоду.

Бот погоды прост в использовании. Он имеет интуитивно понятный пользовательский интерфейс, с помощью 
которого вы сможете получить актуальный прогноз погоды на сегодня, завтра или неделю, всего в один клик. 
Независимо от того, являетесь ли вы опытным пользователем Telegram или только начинаете свое знакомство 
с этой мессенджером, вы легко найдете нужные функции и будите пользоваться ботом без усилий.

Не упустите возможность стать обладателем удивительного Telegram-бота погоды. Подключайтесь сейчас и наслаждайтесь 
актуальным прогнозом погоды и увлекательной информацией о погоде. 
Наш бот погоды – это ваш незаменимый помощник, который всегда будет рядом с вами, чтобы помочь вам планировать 
свой день и быть готовыми ко всем погодным условиям.

## Requirements

Вы можете установить все зависимости, выполнив следующую команду: `pip install -r requirements.txt`

## Команды бота

- `/start` - Запуск бота, выполняется автоматически при подключении к боту.
- `/Отправить геолокацию` - Отправка вашей геопозиции, получение погодных условий по заданному вами периоду.
- `/help` - Описание и подсказка.
- `/today` - Погодные условия на сегодня.
- `/tomorrow` - Погодные условия на завтра.
- `/week` - Погодные условия на неделю.
- `/history` - История запросов пользователя.


## Как работать с ботом

В файле config.py вписать:

`API_TOKEN = "Ваш токен для бота, полученный от @BotFather"`

`OPENWEATHERMAP_API_KEY = "Ваш ключ полученный от API по адресу https://openweathermap.org/"`

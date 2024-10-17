import asyncio, logging, os, pywttr

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from pywttr_models.ru import Model

load_dotenv()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()

def get_weather() -> Model:
    return pywttr.get_weather('Saint-Petersburg', pywttr.Language.RU)

def get_weather_text(weather: Model) -> str:
    weather_item = weather.weather[0]

    return (
        f"Погода в Санкт-Петербурге:\n"
        f"Дата: {weather_item.date}\n"
        f"Температура: {weather_item.mintemp_c}°С - {weather_item.maxtemp_c}°С\n"
        f"Время рассвета: {weather_item.astronomy[0].sunrise}\n"
        f"Время заката: {weather_item.astronomy[0].sunset}"
    )

@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Введи команду /weather, чтобы получить погоду в Санкт-Петербурге.")

@dp.message(Command("weather"))
async def weather_command(message: types.Message):
    weather: Model = get_weather()

    await message.answer(get_weather_text(weather))

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
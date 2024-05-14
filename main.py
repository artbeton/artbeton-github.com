import asyncio
import json

from aiogram import types
from aiogram import Bot, Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command 
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

bot = Bot(token="6841846251:AAGIYkIDeBIO62xQMEvCXHZJCvB2cR8QKGc")
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: types.Message, state: FSMContext):
    
    item1 = KeyboardButton(text="⛲️ Сайт", web_app=WebAppInfo(url="https://artbeton.github.io/artbeton-github.com/"))
    item2 = KeyboardButton(text="✍️ Kanalga kirish", web_app=WebAppInfo(url="https://t.me/fantanuz"))
    item3 = KeyboardButton(text="📌 Manzilga borish", web_app=WebAppInfo(url="https://maps.app.goo.gl/xdo7b7NmNq8PniSv5"))
    keyboard = ReplyKeyboardMarkup (keyboard=[[item1],[item2],[item3]], resize_keyboard=True)
    await bot.send_message(message.from_user.id, "Assalomu aleykum! * Fantanuz * shaxsiy kanalga obuna bulishni unutmang  tugmalardan foydalanib батафсил малумотга танишиб чикинг🙂 Botni qayta ishga tushirish tugmasi /start ", reply_markup=keyboard, parse_mode="Markdown")
    

@dp.message()
async def web_app(callback_query):
    json_data = callback_query.web_app_data.data
    parsed_data = json.loads(json_data)
    message = "Xarid qilganiz uchun raxmat"
    for i, item in enumerate(parsed_data['items'], start=1):
        position = int(item['id'].replace('item', ''))
        message += f"Artikul {position}\n"
        message += f"Narx: {item['price']}\n\n"

    message += f"Jami maxsulot narxi:{parsed_data['totalPrice']}"

    await bot.send_message(callback_query.from_user.name, f""")
{message}
""")
    await bot.send_message('-1002082001380', f"""
Yangi zakaz
{message}
""")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

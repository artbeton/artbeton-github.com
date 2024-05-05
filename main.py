import asyncio
import json

from aiogram import types
from aiogram import Bot, Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command 
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

bot = Bot(token="7165989174:AAF3CzWo1YC8Er2rqK5eraykWd-2nkL9TU0")
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: types.Message, state: FSMContext):
    
    item1 = KeyboardButton(text="⛲️ Сайт", web_app=WebAppInfo(url="https://bahrom88ak.github."))
    item2 = KeyboardButton(text="✍️ Gruxga qushilish", web_app=WebAppInfo(url="https://t.me/fantanuz"))
    keyboard = ReplyKeyboardMarkup (keyboard=[[item1],[item2]], resize_keyboard=True)
    await bot.send_message(message.from_user.id, "Assalomu aleykum! * Faberli3 🛍 * shaxsiy gruxga obuna bulishni unutmang   Men shaxsiy bot xizmatidan foydalanganim sabab ishim juda kup ulgurmayapman, online ishga kirish va sotib olish saxifa mavjud! tugmalardan foydalanib xarid qilish yoki ishga kirishingiz mumkin🙂 Botni qayta ishga tushirish tugmasi /start ", reply_markup=keyboard, parse_mode="Markdown")
    

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

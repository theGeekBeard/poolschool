from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from loader import dp, db


@dp.message_handler(commands=["menu"])
async def show_menu(message: types.Message):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Турниры", url="https://poolschool.ru/oplata-i-registraciya-na-turnir")],
            [InlineKeyboardButton("Услуги", callback_data="services")],
            [InlineKeyboardButton("Контакты", callback_data="contacts")],
            [InlineKeyboardButton("О школе", callback_data="about_school")],
            [InlineKeyboardButton("Заявка на обратную связь", url="https://t.me/poolschooladm")],
        ]
    )

    stock = await db.get_stock()
    if stock[1] == 1:
        markup.add(InlineKeyboardButton("Акции", callback_data="stock"))
    if message.chat.id == 610626273 or message.chat.id == 5294530966:
        markup.row(InlineKeyboardButton("Изменить блок 'Акции'", callback_data="change_stock"))

    await message.answer("Главное меню:", reply_markup=markup)

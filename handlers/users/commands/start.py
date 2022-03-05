from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await db.add_user(message.chat.id)

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
        markup.row(InlineKeyboardButton("Статистика", callback_data="statistic"))

    await message.answer(f"Привет, {message.chat.full_name}. Добро пожаловать в Школу бильярда Poolschool!",
                         reply_markup=markup)

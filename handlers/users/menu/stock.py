from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from loader import dp, db


@dp.callback_query_handler(text="stock")
async def get_additional_buttons(call: CallbackQuery):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Назад", callback_data="back_to_main_menu")]
        ]
    )

    stock = await db.get_stock()

    if stock[1] == 0:
        await call.message.edit_text("В данный момент нет акций", reply_markup=markup)
    else:
        await call.message.edit_text(stock[0], reply_markup=markup)



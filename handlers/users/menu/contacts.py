from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from loader import dp


@dp.callback_query_handler(text=["contacts", "back_to_contacts"])
async def get_additional_buttons(call: CallbackQuery):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Телефон", callback_data="phone_number")],
            [InlineKeyboardButton("WhatsApp", callback_data="whatsapp")],
            [InlineKeyboardButton("Instagram", url="https://www.instagram.com/poolschool.billiard/")],
            [InlineKeyboardButton("Назад", callback_data="back_to_main_menu")]
        ]
    )

    await call.message.edit_text("Контакты", reply_markup=markup)


@dp.callback_query_handler(text="phone_number")
async def get_phone_number(call: CallbackQuery):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Назад", callback_data="back_to_contacts")]
        ]
    )

    await call.message.edit_text("Телефон: +74954100966", reply_markup=markup)


@dp.callback_query_handler(text="whatsapp")
async def get_phone_number(call: CallbackQuery):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Назад", callback_data="back_to_contacts")]
        ]
    )

    await call.message.edit_text("WhatsApp: +79864100966", reply_markup=markup)

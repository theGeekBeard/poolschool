from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from loader import dp


@dp.callback_query_handler(text="about_school")
async def get_additional_buttons(call: CallbackQuery):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Школа бильярда", url="https://poolschool.ru/o-shkole-n")],
            [InlineKeyboardButton("Методика обучения", url="https://poolschool.ru/metodika-obucheniya-n")],
            [InlineKeyboardButton("Назад", callback_data="back_to_main_menu")]
        ]
    )

    await call.message.edit_text("О школе", reply_markup=markup)

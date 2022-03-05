from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from loader import dp, db


@dp.callback_query_handler(text="statistic")
async def ask_change_type(call: CallbackQuery):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Назад", callback_data="back_to_main_menu")]
        ]
    )

    user_count = await db.get_statistic()

    await call.message.edit_text(f"За все время бота запустили {user_count} пользователей", reply_markup=markup)

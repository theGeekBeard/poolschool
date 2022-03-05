from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from handlers.users.commands.menu import show_menu
from loader import dp, db, bot
from states import states


@dp.callback_query_handler(text="change_stock", state="*")
async def ask_change_type(call: CallbackQuery, state: FSMContext):
    await state.finish()

    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Изменить текст и включить блок", callback_data="change_text")],
            [InlineKeyboardButton("Отключить блок", callback_data="stock_off")],
            [InlineKeyboardButton("Назад", callback_data="back_to_main_menu")]
        ]
    )

    await call.message.edit_text("Выберите действие", reply_markup=markup)


@dp.callback_query_handler(text="stock_off")
async def stock_off(call: CallbackQuery):
    await db.change_stock(text="None", status=0)

    await call.answer("Блок отключен")

    await call.message.delete()

    await show_menu(call.message)


@dp.callback_query_handler(text="change_text")
async def ask_stock_text(call: CallbackQuery):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Назад", callback_data="change_stock")]
        ]
    )

    await call.message.edit_text("Введите новый текст", reply_markup=markup)

    await states.Stock.text.set()


@dp.message_handler(state=states.Stock.text)
async def change_stock_text(message: types.Message, state: FSMContext):
    await bot.delete_message(message.chat.id, message.message_id - 1)

    stock_text = message.text

    await db.change_stock(text=stock_text, status=1)

    await message.answer("Текст успешно изменен")

    await show_menu(message)

    await state.finish()

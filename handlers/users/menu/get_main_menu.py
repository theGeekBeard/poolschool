from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from loader import dp, db


@dp.callback_query_handler(text="back_to_main_menu")
async def get_main_menu(call: CallbackQuery):
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
        markup.row(InlineKeyboardButton("Акции", callback_data="stock"))
    if call.message.chat.id == 610626273 or call.message.chat.id == 5294530966:
        markup.row(InlineKeyboardButton("Изменить блок 'Акции'", callback_data="change_stock"))

    await call.message.edit_text("Главное меню", reply_markup=markup)

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menuKeyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Турниры", url="https://poolschool.ru/oplata-i-registraciya-na-turnir")],
        [InlineKeyboardButton("Услуги", callback_data="services")],
        [InlineKeyboardButton("Контакты", callback_data="contacts")],
        [InlineKeyboardButton("О школе", callback_data="about_school")],
        [InlineKeyboardButton("Заявка на обратную связь", url="https://t.me/poolschooladm")],
    ]
)

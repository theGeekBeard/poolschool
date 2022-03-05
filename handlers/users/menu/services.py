from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from loader import dp


@dp.callback_query_handler(text=["services", "back_to_services"])
async def get_additional_buttons(call: CallbackQuery):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Абонементы", callback_data="abonements")],
            [InlineKeyboardButton("Мастер класс", url="https://poolschool.ru/master-klassy-n")],
            [InlineKeyboardButton("День рождения в бильярдном клубе",
                                  url="https://poolschool.ru/den-rozhdeniya-v-klube-bilyarda-n")],
            [InlineKeyboardButton("Сертификаты",
                                  url="https://poolschool.ru/certificate")],
            [InlineKeyboardButton("Назад", callback_data="back_to_main_menu")]
        ]
    )

    await call.message.edit_text("Услуги", reply_markup=markup)


@dp.callback_query_handler(text=["abonements", "back_to_abonemets"])
async def get_phone_number(call: CallbackQuery):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Групповые", callback_data="groups_abonemets")],
            [InlineKeyboardButton("Индивидуальные", url="https://poolschool.ru/pers")],
            [InlineKeyboardButton("Назад", callback_data="back_to_services")]
        ]
    )

    await call.message.edit_text("Абонементы", reply_markup=markup)


@dp.callback_query_handler(text="groups_abonemets")
async def get_phone_number(call: CallbackQuery):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Информация", url="https://poolschool.ru/pricegroup")],
            [InlineKeyboardButton("Оплата абонемента", url="https://poolschool.ru/subscription")],
            [InlineKeyboardButton("Назад", callback_data="back_to_abonemets")]
        ]
    )

    await call.message.edit_text("Группы", reply_markup=markup)

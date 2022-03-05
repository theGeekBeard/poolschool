from aiogram import types

from loader import dp, bot


@dp.message_handler(content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def new_chat_member(message: types.Message):
    await bot.send_message(chat_id=-1001528491240,
                           text=f"Привет, {message.from_user.full_name}. Пиши мне в личные сообщения "
                                f"@pool_school_bot, чтобы подробнее "
                                f"узнать "
                                f"о нашей школе!")

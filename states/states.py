from aiogram.dispatcher.filters.state import StatesGroup, State


class Stock(StatesGroup):
    text = State()



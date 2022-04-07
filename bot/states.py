from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMAddCategory(StatesGroup):
    command = State()
    name = State()


class FSMCategory(StatesGroup):
    categories = State()
    category = State()
    command = State()

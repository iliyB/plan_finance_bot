from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMAddCategory(StatesGroup):
    command = State()
    name = State()


class FSMDelCategory(StatesGroup):
    command = State()
    name = State()

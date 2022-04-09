from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMAddCategory(StatesGroup):
    command = State()
    name = State()


class FSMCategory(StatesGroup):
    categories = State()
    category = State()


class FSMAddTask(StatesGroup):
    category = State()
    description = State()
    planed_time = State()
    timeshift = State()
    links = State()


class FSMDatePeriod(StatesGroup):
    first_date = State()
    second_date = State()

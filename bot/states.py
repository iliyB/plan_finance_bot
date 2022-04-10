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


class FSMTask(StatesGroup):
    tasks = State()
    task = State()


class FSMCompletedTask(StatesGroup):
    feedback = State()
    completed_time = State()
    timeshift = State()


class FSMChangeTask(StatesGroup):
    category = State()
    description = State()
    planed_time = State()
    timeshift = State()


class FSMDatePeriod(StatesGroup):
    first_date = State()
    second_date = State()

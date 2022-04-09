from enum import Enum


class CommandEnum(Enum):
    START = "start"
    HELP = "help"
    RESET = "Отменить"

    CATEGORY_KEYBOARD = "Категории"
    ADD_CATEGORY = "Добавить категорию"
    LIST_CATEGORY = "Мои категории"
    FILTER_CATEGORY = "Фильтрация категорий"
    DEL_CATEGORY = "Удалить категорию"

    TASK_KEYBOARD = "Задачи"
    ADD_TASK = "Добавить задачу"
    LIST_TASK = "Мои задачи"
    FILTER_TASK = "Фильтрация задач"
    DEL_TASK = "Удалить задачу"

    ALL_PLANED_TASKS = "Все задачи"
    TODAY_TASKS = "На сегодня"
    WEEKLY_TASKS = "На ближайшую неделю"
    PERIOD_TIME_TASKS = "В определенном промежутке времени"

    @property
    def value_with_slash(self) -> str:
        return f"/{self.value}"

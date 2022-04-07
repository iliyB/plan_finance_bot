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

    @property
    def value_with_slash(self) -> str:
        return f"/{self.value}"

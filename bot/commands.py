from enum import Enum


class CommandEnum(Enum):
    START = "start"
    HELP = "help"
    RESET = "reset"

    ADD_CATEGORY = "add_category"
    LIST_CATEGORY = "categories"
    DEL_CATEGORY = "del_category"

    @property
    def value_with_slash(self) -> str:
        return f"/{self.value}"

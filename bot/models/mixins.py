from typing import Any

from sqlalchemy import inspect


class EqMixin(object):
    """
    Миксин, используемый для сравнение объектов моделей алхимии
    """

    def compare_value(self) -> int:
        """Return a value or tuple of values to use for comparisons.
        Return instance's primary key by default, which requires that it is persistent in the database.
        Override this in subclasses to get other behavior.
        """
        return inspect(self).identity

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented

        return self.compare_value() == other.compare_value()

    def __ne__(self, other: Any) -> bool:
        eq = self.__eq__(other)

        if eq is NotImplemented:
            return eq

        return not eq

    def __hash__(self) -> int:
        return hash(self.__class__) ^ hash(self.compare_value())

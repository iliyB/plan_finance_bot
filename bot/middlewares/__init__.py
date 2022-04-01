from aiogram import Dispatcher

from .authorization import AuthorizationMiddleware


def setup(dp: Dispatcher) -> None:
    dp.middleware.setup(AuthorizationMiddleware())

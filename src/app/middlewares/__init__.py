from last.dispatcher import CustomDispatcher
from .authorization import AuthorizationMiddleware


def setup(dp: CustomDispatcher):
    dp.middleware.setup(AuthorizationMiddleware())
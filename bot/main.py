from aiogram.utils import executor
from loader import dp

# async def on_startup(dp: CustomDispatcher) -> None:
#     import middlewares
#     middlewares.setup(dp)
#
#     await dp.set_db("my_finance.db")
#
#
# async def on_shutdown(dp: CustomDispatcher) -> None:
#     await dp.close_db()


if __name__ == "__main__":
    # from handlers import dp
    # executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
    executor.start_polling(dp, skip_updates=True)

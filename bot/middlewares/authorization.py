# from aiogram import types
# from aiogram.dispatcher.middlewares import BaseMiddleware
#
# from handlers import dp
#
#
# class AuthorizationMiddleware(BaseMiddleware):
#     async def on_process_message(self, message: types.Message, _):
#         telegram_user_id = int(message.from_user.id)
#
#         user = await dp.get_user_from_telegram(telegram_user_id)
#
#         if not user:
#             await dp.insert("user", {"telegram_user_id": telegram_user_id})
#             user = await dp.get_user_from_telegram(telegram_user_id)
#             await message.answer("Hello!")
#
#         setattr(message, "user", user)

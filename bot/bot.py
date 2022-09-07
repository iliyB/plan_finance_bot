from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from config import configs

redis_url = f"redis://@{configs.REDIS_HOST}:{configs.REDIS_PORT}/{configs.REDIS_DB_FSM}"

redis = RedisStorage.from_url(redis_url)

storage = RedisStorage(redis=redis)

bot = Bot(token=configs.TELEGRAM_API_TOKEN, parse_mode="HTML")
dp = Dispatcher(storage=storage)

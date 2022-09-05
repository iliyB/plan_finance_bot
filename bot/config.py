from typing import Dict, Optional

from pydantic import BaseSettings, Field, root_validator


class PostgresConfigs(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str = Field(..., env="DB_CONTAINER_NAME")
    POSTGRES_PORT: str = Field(..., env="PORT_DB")
    POSTGRES_DB: str


class RedisConfigs(BaseSettings):
    REDIS_HOST: str = Field(..., env="REDIS_CONTAINER_NAME")
    REDIS_PORT: str
    REDIS_DB_FSM: str


class BotConfigs(BaseSettings):
    POLLING: bool = True
    TELEGRAM_API_TOKEN: str
    HOST: Optional[str] = None
    WEBHOOK_PATH: Optional[str] = None
    WEBHOOK_URL: Optional[str] = None

    @root_validator
    def set_webhook(cls, values: Dict) -> Dict:
        if not values.get("HOST") and values.get("POLLING") is False:
            if values.get("WEBHOOK_PATH") and values.get("WEBHOOK_URl"):
                return values
            else:
                raise ValueError("HOST must not be None")

        if values.get("POLLING") is True:
            return values

        values.update(
            {
                "WEBHOOK_PATH": f"/bot/{values.get('TELEGRAM_API_TOKEN')}",
                "WEBHOOK_URl": f"{values.get('HOST')}/bot/{values.get('TELEGRAM_API_TOKEN')}",
            }
        )

        return values


class Configs(PostgresConfigs, RedisConfigs, BotConfigs):
    ...


configs = Configs()

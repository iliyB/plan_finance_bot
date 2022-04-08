from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from bot.models.users import User

UserScheme = sqlalchemy_to_pydantic(User)


class UserCreateScheme(BaseModel):
    user_id: int

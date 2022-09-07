from typing import Optional

from pydantic import BaseModel, Field


class UserCreateSchema(BaseModel):
    user_id: int
    first_name: Optional[str] = Field(None, max_length=64)
    last_name: Optional[str] = Field(None, max_length=64)
    username: str = Field(..., max_length=64)
    language_code: Optional[str] = Field(..., max_length=64)

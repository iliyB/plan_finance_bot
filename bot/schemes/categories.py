from pydantic import BaseModel, Field
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from bot.models.categories import Category

CategoryScheme = sqlalchemy_to_pydantic(Category)


class CategoryNameScheme(BaseModel):
    category_name: str = Field(max_length=32)

from sqlalchemy import Column, ForeignKey, Integer, Table

from bot.core.database import Base

UserCategory = Table(
    "user_category_associated",
    Base.metadata,
    Column("user_id", ForeignKey("user.user_id")),
    Column("category_id", ForeignKey("category.category_id")),
)

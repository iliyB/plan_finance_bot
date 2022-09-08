from core.database import Base
from models.many_to_many import UserCategoryAssociatedTable
from models.mixins import EqMixin
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Category(Base, EqMixin):
    __tablename__ = "category"

    category_id = Column(Integer, primary_key=True)
    category_name = Column(String, unique=True)
    users = relationship(
        "User", secondary=UserCategoryAssociatedTable, back_populates="categories"
    )
    tasks = relationship("Task", back_populates="category")

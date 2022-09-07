from core.database import Base
from models.many_to_many import UserCategory
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = "category"

    category_id = Column(Integer, primary_key=True)
    category_name = Column(String, unique=True)
    users = relationship("User", secondary=UserCategory, back_populates="categories")
    tasks = relationship("Task", back_populates="category")

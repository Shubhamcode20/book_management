
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text
from app.database import Base


class Books(Base):
    __tablename__ = "books"

    id = Column(Integer,primary_key=True,nullable=False)
    title = Column(String,nullable=False)
    author = Column(String, nullable=False)
    published_year = Column(Integer, nullable=False)
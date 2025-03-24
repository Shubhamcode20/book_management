from pydantic import BaseModel
class BooksBase(BaseModel):
    title :str
    author : str
    published_year : int

    class Config:
        orm_mode = True

class CreateBooks(BooksBase):
    class Config:
        orm_mode = True
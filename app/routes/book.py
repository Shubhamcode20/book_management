from fastapi import APIRouter, HTTPException

from app import schemas, models
from app.database import get_db
from app.services.book import create_book
from typing import List
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
from fastapi import APIRouter

router = APIRouter()

@router.get('/', response_model=List[schemas.CreateBooks])
def get_books(db: Session = Depends(get_db)):
    book = db.query(models.Books).all()
    return book

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=List[schemas.CreateBooks])
def create_book(books_post:schemas.CreateBooks, db:Session = Depends(get_db)):

    new_book = models.Books(**books_post.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return [new_book]


@router.get('/{id}', response_model=schemas.CreateBooks, status_code=status.HTTP_200_OK)
def get_book_by_id(id:int ,db:Session = Depends(get_db)):

    idv_book = db.query(models.Books).filter(models.Books.id == id).first()

    if idv_book is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"The id: {id} you requested for does not exist")
    return idv_book

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_book(id:int, db:Session = Depends(get_db)):

    deleted_book = db.query(models.Books).filter(models.Books.id == id)


    if deleted_book.first() is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"The id: {id} you requested for does not exist")
    deleted_book.delete(synchronize_session=False)
    db.commit()



@router.put('/{id}', response_model=schemas.CreateBooks)
def update_book(update_books:schemas.BooksBase, id:int, db:Session = Depends(get_db)):
    updated_book =  db.query(models.Books).filter(models.Books.id == id)

    if updated_book.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The id:{id} does not exist")
    updated_book.update(update_books.dict(), synchronize_session=False)
    db.commit()


    return  updated_book.first()
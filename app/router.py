from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import BookSchema, RequestBook, Responce
import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/create')
async def create(request: RequestBook, db:Session = Depends(get_db)):
    _book= crud.create_book(db,request.parameter)
    return Responce(code="200", status="OK", message="Book created successfully", result=_book).dict(exclude_none=True)


@router.get("/")
async def get(db:Session=Depends(get_db)):
    _book = crud.get_book(db,0,100)
    return Responce(code="200", status="OK", message="All book fetch successfully", result=_book).dict(exclude_none=True)


@router.get("/{id}")
async def get_by_id(id:int, db:Session=Depends(get_db)):
    _book = crud.get_book_by_id(db,id)
    return Responce(code="200", status="OK", message="book fetch successfully", result=_book).dict(exclude_none=True)


@router.put("/update")
async def update_book(request: RequestBook, db:Session = Depends(get_db)):
    _book = crud.update_book(db, book_id=request.parameter.id, title=request.parameter.title, description=request.parameter.description)
    return Responce(code="200", status="OK", message="book update successfully", result=_book).dict(exclude_none=True)  


@router.delete("/delete{id}")
async def delete_book(id:int, db:Session = Depends(get_db)):
    _book = crud.remove_book(db, book_id=id)
    return Responce(code="200", status="OK", message="book deleted successfully", result=_book).dict(exclude_none=True)  
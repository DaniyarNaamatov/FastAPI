from typing import List

from fastapi import FastAPI, Query, Path, Body
from schemas import Books, Author

app = FastAPI()

@app.get('/')
def home():
    return {
        "key": "hello"
    }

@app.get('/{pk}')
def get_item(pk: int, q: str = None):
    return {"key": pk, "q": q}


@app.get('/user/{pk}/items/{item}')
def get_user_item(pk: int, item: str):
    return {"user": pk, "item": item}


@app.post('/books')
def create_book(item: Books, author: Author, quantity: int = Body(...)):
    return {"item": item, "author": author, "quantity": quantity}




@app.post('/author')
def create_author(author: Author = Body(..., embed=True)):
    return {"author": author}



@app.get('/books')
def get_book(q: List[str] = Query("test", description="Search books", deprecated=True)):
    return q


@app.get('/books/{pk}')
def get_single_book(pk: int = Path(..., gt=1, le=20), pages: int = Query(None, gt=10, le=500)):
    return {"pk": pk, "pages": pages}




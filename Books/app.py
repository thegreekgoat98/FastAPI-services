from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel

client = MongoClient("mongodb://localhost:27017/Books")
db = client.Books
myDB = db.chinmoy
app = FastAPI()


class Books(BaseModel):
    book_id: int
    book_name: str
    book_author: str
    book_price: float


@app.get("/")
def home():
    return "This is for BookStore"


@app.get("/show")
def show():
    # result = list(myDB.find({}))
    # final_list = []
    # for books in result:
    #     del books["_id"]
    #     final_list.append(books)
    # return {"Book Details : ": final_list}

    collection_data = list(myDB.find({}, {'_id': False}))
    return collection_data


@app.post("/add")
def add(book: Books):
    if list(myDB.find({"book_id": book.book_id})) == []:
        myDB.insert_one(book.dict())
        return {"Success": "Book added successfully"}
    else:
        return {"Error": "Book cannot add because same book_id is present"}


@app.put("/update/{book_id}")
def update(book_id: int, book: Books):
    if list(myDB.find({"book_id": book_id})) == []:
        return {"Error": "book_id not present in the details"}
    else:
        myDB.update_one({"book_id": book_id}, {"$set": book.dict()})
        return {"Success": "Updated Successfully"}


@app.delete("/delete/{book_id}")
def delete(book_id: int):
    if list(myDB.find({"book_id": book_id})) == []:
        return {"Error": "Cannot Delete, book_id not present"}
    else:
        myDB.delete_one({"book_id": book_id})
        return {"Success": "Deleted Successfully"}

import self
from fastapi import FastAPI

app =  FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

BOOKS = [
    Book(1, "The Great Gatsby", "F. Scott Fitzgerald", "A novel set in the Roaring Twenties.", 5),
    Book(2, "To Kill a Mockingbird", "Harper Lee", "A novel about racial injustice in the Deep South.", 5),
    Book(3, "1984", "George Orwell", "A dystopian novel about totalitarianism.", 4),
    Book(4, "Pride and Prejudice", "Jane Austen", "A classic romance novel.", 5),
    Book(5, "The Catcher in the Rye", "J.D. Salinger", "A novel about teenage rebellion.", 4)
]


@app.get("/books")
async def read_all_books():
    return BOOKS
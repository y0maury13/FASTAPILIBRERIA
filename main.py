from fastapi import FastAPI, HTTPException
from models import Book

app = FastAPI()

# Base de datos ficticia
books_db = []

# Obtener todos los libros
@app.get("/books/", response_model=list[Book])
def get_books():
    return books_db

# Obtener un libro por ID
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# Crear un nuevo libro
@app.post("/books/", response_model=Book)
def create_book(book: Book):
    books_db.append(book)
    return book

# Actualizar un libro existente
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(books_db):
        if book.id == book_id:
            books_db[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

# Eliminar un libro
@app.delete("/books/{book_id}", response_model=Book)
def delete_book(book_id: int):
    for index, book in enumerate(books_db):
        if book.id == book_id:
            return books_db.pop(index)
    raise HTTPException(status_code=404, detail="Book not found")

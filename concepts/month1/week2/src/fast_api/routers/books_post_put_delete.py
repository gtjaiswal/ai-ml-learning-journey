from fastapi import FastAPI, Body, APIRouter

books_Post_put_delete_router = APIRouter()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'science'}
]

@books_Post_put_delete_router.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return {"message": "Book added", "book": new_book}

@books_Post_put_delete_router.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i, book in enumerate(BOOKS):
        if book.get('title') == updated_book.get('title'):
            BOOKS[i] = updated_book
            return {"message": "Book updated successfully", "book": updated_book}
    return {"message": "Book not found"}

@books_Post_put_delete_router.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i, book in enumerate(BOOKS):
        if book.get('title') == book_title:
            deleted_book = BOOKS.pop(i)
            return {"message": "Book deleted successfully", "upfstedlist": BOOKS}
    return {"message": "Book not found"}

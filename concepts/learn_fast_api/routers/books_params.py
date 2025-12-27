from fastapi import APIRouter
from scalar_fastapi import get_scalar_api_reference

books_param_router = APIRouter()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'science'}
]

@books_param_router.get("/books/my_book")
async def read_book_by_title():
    print("read_book_by_title")
    return (book for book in BOOKS if book["title"]=="Title Two")

# Path Param
@books_param_router.get("/books/{book_title}")
async def read_book_by_title(book_title: str):
    print("read_book_by_title")
    book = next((book for book in BOOKS if book['title'] == book_title), None)
    return book

# Query Param
@books_param_router.get("/books/")
async def read_books_by_category(category:str):
    books = [book for book in BOOKS if book['category'] == category]
    return books

# Query and Path Params
@books_param_router.get("/books/{author_name}/")
async def read_author_books_by_category(author_name:str, category:str):
    print("read_author_books_by_category", author_name)
    books = [book for book in BOOKS if (book['author'] == author_name and book['category'] == category)]
    return books

@books_param_router.get("/books/{author_name}")
async def read_books_by_author(author_name:str):
    print("read_books_by_author",author_name )
    books = [book for book in BOOKS if (book['author']==author_name)]
    return books

@books_param_router.get("/scalar", include_in_schema=False)
async def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url="/openapi.json",
        title="Scalar API"
    )
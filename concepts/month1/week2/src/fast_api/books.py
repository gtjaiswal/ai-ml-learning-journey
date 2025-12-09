from fastapi import FastAPI
from concepts.month1.week2.src.fast_api.routers import books_params, books_post_put_delete

books_app = FastAPI()

books_app.include_router(books_params.books_param_router)
books_app.include_router(books_post_put_delete.books_Post_put_delete_router)

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

# @books_app.get("/api-endpoint")
# async def first_api():
#     return {"message":"Hello FastAPI"}

@books_app.get("/books")
async def read_all_books():
    return BOOKS



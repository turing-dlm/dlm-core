from django.shortcuts import render
from django.http import JsonResponse
from core.models import UserData
from .models import Book

# Sample api to read from tenant dependent and independent table. will be removed later

def index(request):
    connect_to_schema()
    usersList = UserData.objects.all();
    users = []
    for user in usersList:
        users.append(user.firstname)
    booksList = Book.objects.all();
    books = []
    for book in booksList:
        books.append(book.title)
    response_object = {
            "users" : users,
            "books" : books
        }
    return JsonResponse(response_object, safe=False)


def connect_to_schema():
    from django.db import connection
    with connection.cursor() as cursor:
    # set your schema name here
      cursor.execute(f"SET search_path to dlm1, public")
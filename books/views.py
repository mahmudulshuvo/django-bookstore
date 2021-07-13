import json

from django.http import HttpResponse
from django.shortcuts import render

books = open(r'D:\DjangoRevise\bookstore\bookstore\books.json').read()
data = json.loads(books)

def index(request):
    return render(request, 'books/index.html', {'books': data})

def show(request, id):
    showBook = {}
    for book in data:
        if book['id'] == id:
            showBook = book
    return render(request, 'books/show.html', {'book': showBook})

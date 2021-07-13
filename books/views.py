import json

from django.http import HttpResponse
from django.shortcuts import render

books = open(r'D:\DjangoRevise\bookstore\bookstore\books.json').read()
data = json.loads(books)

def index(request):
    return render(request, 'books/index.html', {'books': data})

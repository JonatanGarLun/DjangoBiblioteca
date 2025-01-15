from django.shortcuts import render

from books.models import Book


# Create your views here.

def index(request):
    latest_books = Book.objects.order_by('-pub_date')[:5]
    return render(request, template_name= "author_list.html", context={"latest_books":latest_books})
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from books.models import Book, Author, Genre


# Create your views here.

@login_required
def booklist(request):
    latest_books = Book.objects.order_by('-publish_date')[:5]
    return render(request, template_name= "book_list.html", context={"latest_books":latest_books})

def bookdetails(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, template_name= "book_details.html", context={"book":book})

@login_required
def authorlist(request):
    latest_authors = Author.objects.order_by('-birth_date')[:5]
    return render(request, template_name="author_list.html", context={"latest_authors":latest_authors})


@login_required
def authordetails(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, template_name="author_details.html", context={"author":author})

@login_required
def genrelist(request):
    latest_genres = Genre.objects.all()
    return render(request, template_name="genre_list.html", context={"latest_genres":latest_genres})

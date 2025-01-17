from django.shortcuts import render, get_object_or_404

from books.models import Book, Author


# Create your views here.

def author_index(request):
    latest_authors = Author.objects.order_by('-birth_date')[:5]
    return render(request, template_name= "books/authors_list.html", context={"latest_authors": latest_authors})

def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, "books/author_details.html", context={"author": author})


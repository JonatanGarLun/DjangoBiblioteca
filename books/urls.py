from books import views

from django.urls import path

app_name = 'books'
urlpatterns = [

        path("", views.booklist, name='booklist'),
        path("<int:book_id>", views.bookdetails, name='bookdetails'),
        path("autores/", views.authorlist, name='authorlist'),
        path("autores/<int:author_id>", views.authordetails, name='authordetails'),
        path("genres/", views.genrelist, name='genrelist'),

]
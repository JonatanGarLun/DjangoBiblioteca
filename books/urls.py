from books import views

from django.urls import path

app_name = 'books'
urlpatterns = [

        path("", views.booklist, name='booklist'),
        path("<int:book_id>", views.bookdetails, name='bookdetails'),
        path("", views.authorlist, name='authorlist'),
        path("<int:author_id>", views.authordetails, name='authordetails'),

]
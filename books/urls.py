from books import views

from django.urls import path

app_name = 'books'
urlpatterns = [

        path("", views.author_index, name='author_index'),

]
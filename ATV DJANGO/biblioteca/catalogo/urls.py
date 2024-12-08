from django.urls import path
from .views import (
    autor_list, autor_create, autor_update, autor_delete,
    livro_list, livro_create, livro_update, livro_delete
)

urlpatterns = [
    path('autores/', autor_list, name='autor_list'),
    path('autores/novo/', autor_create, name='autor_create'),
    path('autores/editar/<int:pk>/', autor_update, name='autor_update'),
    path('autores/deletar/<int:pk>/', autor_delete, name='autor_delete'),
    path('livros/', livro_list, name='livro_list'),
    path('livros/novo/', livro_create, name='livro_create'),
    path('livros/editar/<int:pk>/', livro_update, name='livro_update'),
    path('livros/deletar/<int:pk>/', livro_delete, name='livro_delete'),
]
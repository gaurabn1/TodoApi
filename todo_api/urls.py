from django.urls import path
from .views import *

urlpatterns = [
    path('view-todos/', view_todo, name="view_todo"),
    path('create-todo/', create_todo, name="create_todo"),
    path('update-todo/<int:id>/', update_todo, name="update_todo"),
    path('delete-todo/<int:id>/', delete_todo, name="delete_todo"),
]

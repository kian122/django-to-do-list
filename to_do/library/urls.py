from django.urls import path
from .views import index, create_index , update_view , delete_index , create_user , error

urlpatterns = [
    path('create_user' , create_user , name="user_create"),
    path('', index),
    path('error' , error),
    path('create', create_index ),
    path('<str:pk>/delete', delete_index , name="delete"),
    path('<str:pk>/update', update_view , name="update"),
]

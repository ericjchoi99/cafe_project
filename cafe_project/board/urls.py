from django.urls import path
from . import views

urlpatterns = [
    path('read/', views.board_read, name="board_read"),
    path('read/<int:pk>', views.board_read_one, name="board_read_one"), #int = 정수 (integer)
    path('create/', views.board_create, name = "board_create"),
    path('update/<int:pk>', views.board_update, name = "board_update"),
    path('delete/<int:pk>', views.board_delete, name = "board_delete"),
    path('pre_update/<int:pk>', views.pre_update, name='pre_update'),
   
    
]
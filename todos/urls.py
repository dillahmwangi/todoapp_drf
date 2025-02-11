from todos.views import  TodoDetailAPIView, TodosAPIView
from django.urls import path



urlpatterns = [
    path('', TodosAPIView.as_view(), name='todos'),
    path('<int:id>', TodoDetailAPIView.as_view(), name='todo')
    
    # path('create', CreateTodoAPIView.as_view(), name='create-todo'),
    # path('list', TodoListAPIView.as_view(), name='list-todo')
]
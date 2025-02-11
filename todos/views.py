
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from todos.models import Todo
from todos.pagination import CustomPageNumberPagination
from todos.serializers import TodoSerializer
from django_filters.rest_framework import DjangoFilterBackend

class TodosAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    
    filterset_fields = ['id', 'title','is_complete']
    search_fields = ['id', 'title','is_complete']
    ordering_fields = ['id', 'title','is_complete']
    
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)
    
    
    
class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    
    
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)
    


# class CreateTodoAPIView(CreateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = TodoSerializer
    
#     def perform_create(self, serializer):
#         return serializer.save(owner=self.request.user)
    

# class TodoListAPIView(ListAPIView):
#     serializer_class = TodoSerializer
#     permission_classes = [IsAuthenticated]
    
    
#     def get_queryset(self):
#         return Todo.objects.filter(owner=self.request.user)
    

    
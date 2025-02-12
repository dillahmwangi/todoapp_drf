
from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from todos.models import Todo


class TestListCreateTodos(APITestCase):
    
    def authenticate(self):
        self.client.post(reverse('register'),{
            'username': 'username','email':'email@gmail.com','password':'password'
        })
        
        response = self.client.post(reverse('register'),{
            'username': 'username','email':'email@gmail.com','password':'password'
        })
        
        self.client.credentials(HTTP_AUTHORIZATION =f"Bearer {response.data['token']}")
        print(response.data)
    
    def test_should_not_create_user_with_no_auth(self):
        sample_todo = {'title':'Hello', 'desc': 'Test'}
        response = self.client.post(reverse('todos'), sample_todo)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_should_create_todo(self):
        self.authenticate()
        previous_todo_count = Todo.objects.all().count()
        
        sample_todo = {'title':'Hello', 'desc': 'Test'}
        response = self.client.post(reverse('todos'), sample_todo)
        self.assertEqual(Todo.objects.all().count(),previous_todo_count+1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'],'Hello')
        self.assertEqual(response.data['desc'],'Test')
        
        
    def test_retrieves_all_todos (self):
        self.authenticate()
        response = self.client.get(reverse('todos'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance (response.data['results'], list)
        
        sample_todo = {'title': "Hello", "desc": "Test"}
        self.client.post(reverse ('todos'), sample_todo)
        
        res = self.client.get(reverse('todos'))
        self.assertIsInstance(res.data['count'],int)
        self.assertEqual(res.data['count'],1)
        
        
        
class TestTodoDetailView(APITestCase):
    
    def test_retrieves_one_item(self):
         pass
    
    def test_updates_one_item(self):
        pass
    
    def test_delete_one_item(self):
        pass
        

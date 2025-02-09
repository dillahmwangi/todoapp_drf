from rest_framework.test import APITestCase
from authentication.models import User

class TestModel(APITestCase):
    
    def test_creates_user(self):
        user=User.objects.create_user('dillah','dillah@gmail.com','dillah123')
        self.assertIsInstance(user,User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email,'dillah@gmail.com')
        
        
        
    def test_creates_super_user(self):
        user=User.objects.create_superuser('dillah','dillah@gmail.com','dillah123')
        self.assertIsInstance(user,User) 
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email,'dillah@gmail.com')
        
        
    def test_raises_error_when_no_username_is_supplied(self):
        self.assertRaises(ValueError,User.objects.create_user,username="",email='dillah@gmail.com',password='dillah123')
       
        
    def test_raises_error_when_no_username_is_supplied(self):
        with self.assertRaisesMessage(ValueError,'Username must be set'):
            User.objects.create_user(username="",email='dillah@gmail.com',password='dillah123')


    def test_raises_error_when_no_email_is_supplied(self):
        self.assertRaises(ValueError,User.objects.create_user,username="username",email='',password='dillah123')
       
        
    def test_raises_error_with_message_when_no_email_is_supplied(self):
        with self.assertRaisesMessage(ValueError,'Email must be set'):
            User.objects.create_user(username="username",email='',password='dillah123')


    def test_cant_creates_super_user_with_no_is_staff_status(self):
        with self.assertRaisesMessage(ValueError,'Superuser must have is_staff=True.'):
            User.objects.create_superuser(username="username",email='dillah@gmail.com',password='dillah123',is_staff=False)


    def test_cant_creates_super_user__with_no_super_user_status(self):
        with self.assertRaisesMessage(ValueError,'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(username="username",email='dillah@gmail.com',password='dillah123',is_superuser=False)
from rest_framework import exceptions
import jwt
from authentication.models import User
from django.conf import settings
from rest_framework.authentication import get_authorization_header, BaseAuthentication



class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = get_authorization_header(request)
        
        auth_date = auth_header.decode('utf-8')
        
        auth_token= auth_date.split(" ")
        
        if len(auth_token) !=2:
            raise exceptions.AuthenticationFailed('Token Not Valid')
        
        token = auth_token[1]
        
        try:
            
            payload = jwt.decode(
                token,settings.SECRET_KEY, algorithms="HS256")
            
            username = payload['username']
            
            user = User.objects.get(username=username)
            
            return(user,token)
            
        except jwt.ExpiredSignatureError as ex:
            raise exceptions.AuthenticationFailed(
                'Token is expired, Login again'
            )
            
        except jwt.DecodeError as ex:
            raise exceptions.AuthenticationFailed(
                'Token is invalid'
            )
        except User.DoesNotExist as no_user:
            raise exceptions.AuthenticationFailed(
                'No such User'
            )
            
        return super().authenticate(request)

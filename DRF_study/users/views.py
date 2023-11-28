from django.shortcuts import render

# Create your views here.


from django.contrib.auth.models import User
from rest_framework import generics

from .serializers import RegisterSerializer



# 회원가입을 하는데 있어 , post만 필요하기에
# createAPIView 사용
class RegisterView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = RegisterSerializer
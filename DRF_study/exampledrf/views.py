# django.shortcuts , render는 django의 기본이므로// 지운다
# from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets , permissions , generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view


# 데코레이터 - @api_view사용 
# 함수의 성격을 지정해준다 - ex) get,post.etc..

@api_view(['GET'])
def HelloAPI(request):
  return Response("hello world!")
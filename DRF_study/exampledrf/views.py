# django.shortcuts , render는 django의 기본이므로// 지운다
# from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets , permissions , generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from rest_framework.generics import get_object_or_404
from .models import Book
from .serializers import BookSerializer


# 데코레이터 - @api_view사용 
# 함수의 성격을 지정해준다 - ex) get,post.etc..

# 기본 GET api 

@api_view(['GET'])
def HelloAPI(request):
  
  return Response("hello world!")

# 위의 HelloAPI를 클래스형 뷰로 작성

# class HelloAPI(APIView):
#   def get(self, request):
#     return Response("hello world!")




# fbv - 함수형으로 선언

# 도서 들 api 

@api_view(['GET','POST'])

def booksAPI(request):
  if request.method =='GET':
    books = Book.objects.all()
    # many = True를 넣어줌으로써 , all()로 가져온 여러 개체 대해서 serialize 가능
    serializer = BookSerializer(books , many =True)
    print("request.method" , request.method)

    return Response(serializer.data , status=status.HTTP_200_OK)
  elif request.method =='POST':
    serializer = BookSerializer(data = request.data)

    if serializer.is_valid():
      serializer.save()
      return Response (serializer.data , status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
# 도서 각각의 api

@api_view(['GET'])

def bookAPI(request,bid):
  # get_object_or_404  : 알맞는 것이 있으면 가져오고 , 없다면 에러처리
  book = get_object_or_404(Book , bid=bid)
  serializer = BookSerializer(book)
  return Response(serializer.data , status=status.HTTP_200_OK)




#cbv -클래스형으로 선언 

# 도서 들 api 

class BooksAPI(APIView):
  def get(self,request):
    books = Book.objects.all()
    serializer = BookSerializer(books,many = True)
    return Response(serializer.data , status=status.HTTP_200_OK)
  def post(self,request):
    serializer = BookSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data , status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  


# 도서 각각 api 

class BookAPI (APIView):

  def get(self,request,bid):
    book = get_object_or_404(Book ,bid=bid)
    serializer = BookSerializer(book)
    return Response(serializer.data , status=status.HTTP_200_OK)




  

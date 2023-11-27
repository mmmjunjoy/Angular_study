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


# 중복을 방지하기 위해, mixins 사용
from rest_framework import mixins

# viewset

from rest_framework import viewsets



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




# mixins 사용  -> 사용하니 , delete버튼부터  , put - 업데이트 할 수 있는 폼까지 생성이 되어 편리해졌다.

# 전체에 대한 , get ,post

class BooksAPIMixins(mixins.ListModelMixin , mixins.CreateModelMixin , generics.GenericAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

  def get(self,request, *args, **kwargs):
    return self.list(request,*args,**kwargs)
  
  def post(self,request,*args,**kwargs):
    return self.create(request, *args, **kwargs)

  

# 각각에 대한 api  - 책 1권에 대한 것

# 수정 , 삭제 도 포함

class BookAPIMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  lookup_field = 'bid'

  def get(self,request, *args, **kwargs):
    return self.retrieve(request, *args,**kwargs)
  
  def put(self ,request, *args,**kwargs):
    return self.update(request,*args,**kwargs)
  
  def delete(self, request,*args,**kwargs):
    return self.destroy(request,*args,**kwargs)




# mixins 만으로도 간편함이 해소가 안될떄 , generics를 사용하여 더 간편하게 구현할 수 있다

# generics - 세트라고 생각

# get ,post put, delete등의 기능을 묶어서 쓸 수 있는 함수 형태가 있다.

# 이때는 , 심지어 return 코드도 쓰지않아도 된다 -> 내부코드에서 실행


class BooksAPIGenerics(generics.ListCreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

class BookAPIGenerics(generics.RetrieveUpdateDestroyAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  lookup_field = 'bid'



  # drf ViewSet , Router 
  # - > viewset을 사용한다면 , 단 3줄로 rest api를 구성

class BookViewSet(viewsets.ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
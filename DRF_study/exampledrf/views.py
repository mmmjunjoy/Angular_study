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
from django.http import HttpResponse, JsonResponse


# 중복을 방지하기 위해, mixins 사용
from rest_framework import mixins

# viewset

from rest_framework import viewsets


from django.shortcuts import render
from django.conf import settings

import datetime
import requests


# settings.py 로 부터 API_KEY를 받아온다 

API_KEY = settings.API_KEY


# openapi - 기상청 날씨예보 실습을 위한 함수

def openapi(request):
  url = ' http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?'
  service_key = API_KEY
  today = datetime.datetime.today()
  base_date = today.strftime("%Y%m%d")
  print("basedate" , base_date)
  base_time = "0800"
  nx = '60'
  ny = '128'

  payload = "ServiceKey=" + service_key + "&" +\
  "dataType=json" + "&" +\
  "base_date=" + base_date + "&" +\
  "base_time=" + base_time + '&' +\
  "nx=" + nx + "&" +\
  "ny=" + ny

  response = requests.get(url + payload)

  print("응답" , response)

  #-- 응답은 잘된다---

  items = response.json()


  print("진짜값" , items)

  return JsonResponse(items)



# apiView를 사용해서 , openapi함수 변경 -> weatherAPI

# @api_view(['GET']) -> 하위 함수에서 get요청인지 체크하고 아닐경우 , json형태로 에러 반환한다.
@api_view(['GET'])
def weather(request):
    url = ' http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?'
    service_key = API_KEY
    today = datetime.datetime.today()
    base_date = today.strftime("%Y%m%d")
    print("basedate" , base_date)
    base_time = "0800"
    nx = '60'
    ny = '128'

    # PAYLOAD 변수명 정확하게 해줘야 한다.
    payload = "ServiceKey=" + service_key + "&" +\
    "dataType=json" + "&" +\
    "base_date=" + base_date + "&" +\
    "base_time=" + base_time + '&' +\
    "nx=" + nx + "&" +\
    "ny=" + ny

    response = requests.get(url + payload)

    print("응답" , response)

    #-- 응답은 잘된다---

    items = response.json()


    print("진짜값" , items)

    # Response로 받지 않고  , jsonresponse로 받을 경우 -> drf 적용이 안된다.
    return Response(items)

  


# channel talk api - GET (Channel)

# channel talk open api를 사용하기 위해서는 , 
# Header 에 필수로 key 와 secret 값이 필요하다

# https://api.channel.io/open/v4/channel

@api_view(['GET'])

def ChannelAPI (request):
  url = 'https://api.channel.io/open/v4/channel?'

  headers = {'accept':'application/json' , 'x-access-key':'656977c03efa8f4d07ce' , 'x-access-secret':'753220962e31425ebc56db5f90f0dcc9' }


  response = requests.get(url , headers=headers)

  print("응답" , response)
  
  items = response.json()

  res = items['channel']


  print("응답 값" , items)


  return Response(res)



# channel talk 요구사항에 부합하는 api - single user api사용
# payload로 userid값을 url 뒤에 붙이기

# https://api.channel.io/open/v4/users/@{memberId} 

# ** {} 안에 값을 채울때는 .format()을 사용하면 된다.

@api_view(['GET'])

def singleuserAPI (request):

  memberId = 'e4f4c27d-6810-4f8b-8c40-2034f7c3137a'

  url = 'https://api.channel.io/open/v4/users/@{}'.format(memberId)

  headers = {'accept':'application/json' , 'x-access-key':'656977c03efa8f4d07ce' , 'x-access-secret':'753220962e31425ebc56db5f90f0dcc9'  }

  response = requests.get(url, headers=headers)

  print("응답" , response)
  
  items = response.json()

  print("응답 값" , items)

  # 필요한 값 추출 - profilemallId

  res = items['user']['profile']['mallId']
  
  print("---------------------------------------------------------------------")
  print(" profile.mallID --> " ,res )


  return Response(items)



# 한번에 모든 user의 mallID를 추출하기 위한 API사용

@api_view(['GET'])

def alluserAPI(request):

  url = 'https://api.channel.io/open/v5/user-chats?'

  headers = {'accept':'application/json' , 'x-access-key':'656977c03efa8f4d07ce' , 'x-access-secret':'753220962e31425ebc56db5f90f0dcc9' ,'limit':'499' ,'sortOrder' :'ASC'  }

  # Query paramter 사용 - > limit :500 최대로 하면 , 
  
  # 기존 25개에서 -> 140개정도로 상승

  LIMIT = '500'

  state = 'closed'

  payload = "limit=" + LIMIT
  


  response = requests.get(url + payload,headers=headers)

  print("응답" , response)

  
  items = response.json()

  # itmes['users] 에 mall들이 담긴다.
  # 이것을 for문 이용해서 추출해야된다 
  # res = items['users'][0]['profile']['mallId']  - > 여기서 [0] 인덱스 사용하여 추출

  alluser = items['users']

  alluserlen = len(items['users'])

  print("전체 user 길이",alluserlen)

  alluserlist = []

  ocnt = 0
  xcnt = 0
  nothavemalllist = []
  nothavemallid = []

  for i in range(len(items['users'])):
    # profile에 mallId키가 존재한다면, 리스트에 포함
    
    if 'mallId' in items['users'][i]['profile']:
      alluserlist.append( items['users'][i]['profile']['mallId'])
      ocnt += 1
    else:
      nothavemalllist.append( items['users'][i]['profile'])
      nothavemallid.append(i)
      xcnt += 1
  
  print("---------------------------------------------------------")
  
  print("mallid가지고 있는 업체 정보" , alluserlist)
  print("mallid 가지고 있는 업체 수" , ocnt)


  print("---------------------------------------------------------")

  print("mallid 안가지고 있는 업체 정보" , nothavemalllist)
  print("mallid 안가지고 있는 업체 수" , xcnt)
  print("mallid 안가지고 있는 업체 리스트" , nothavemallid)

  print("---------------------------------------------------------")


  items = items['users'][0]

  return Response(items)



# 위의 api를 사용하면, userchat을 사용하고 있는 업체에 대해서만 추출이 되는거같아
# api 2개를 연이어 사용하는 것으로 해결하고자 함  

# Get a single Group - api

@api_view(['GET'])

def groupAPI (request):

  url = ' https://api.channel.io/open/v4/groups/332694?'

  headers = {'accept':'application/json' , 'x-access-key':'656977c03efa8f4d07ce' , 'x-access-secret':'753220962e31425ebc56db5f90f0dcc9'  }

  response = requests.get(url, headers=headers)

  print('응답', response)

  items = response.json()

  return Response(items)















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
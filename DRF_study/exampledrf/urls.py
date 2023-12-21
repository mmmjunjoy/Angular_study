from django.urls import path,include
from .views import HelloAPI ,bookAPI,booksAPI ,BookAPI ,BooksAPI,BookAPIMixins,BooksAPIMixins,BooksAPIGenerics,BookAPIGenerics , BookViewSet , weather ,ChannelAPI,singleuserAPI ,alluserAPI,groupAPI ,userupdateAPI,webhooks

# viewset - url 사용

from rest_framework import routers

from . import views

urlpatterns = [
  path("hello/",HelloAPI),
  path("fbv/books/", booksAPI),
  path("fbv/book/<int:bid>/", bookAPI),
  path("cbv/books/" , BooksAPI.as_view()),
  path("cbv/book/<int:bid>/" , BookAPI.as_view()),
  path("mixin/books/", BooksAPIMixins.as_view()),
  path("mixin/book/<int:bid>/", BookAPIMixins.as_view()),
  path("generics/books/",BooksAPIGenerics.as_view() ),
  path("generics/book/<int:bid>/" , BookAPIGenerics.as_view() ),
  path('openapi/' , views.openapi, name = 'openapi_wheather'),
  path('Weatherapi/' , weather),
  path('Channelapi/' , ChannelAPI),
  path('singleuser/' ,singleuserAPI),
  path('alluser/' ,alluserAPI),
  path('groupuser/' ,groupAPI),
  path('updateuser/',userupdateAPI),
  path('webhook/' , webhooks)
]


router = routers.SimpleRouter()
router.register('books',BookViewSet)

# 아래를 사용할 경우 -> viewset을 사용한다는 의미 , 위의 urlpattern은 자동적으로 사용 x
# urlpatterns = router.urls



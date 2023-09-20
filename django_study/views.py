
#웹페이지에서 보기 위한 방법


from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def index(request):
  return HttpResponse('hello')


def posts(request):
  posts= Post.objects.filter(published_ata_isnull==False).order_by('-published_at')
  return render(request, 'blog/posts.html',{'posts':posts})


from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib import auth
from django.contrib.auth import authenticate

def index(request):
    return HttpResponse("Hello, world. ")



# django에서 로그인 기능을 구현할 수 있는 것은 , 
# AuthenticationForm이라는 내장된 기능도 있음.


#로그인 

def loginsaladlab(request):

    okay = False
    if request.method == "POST":
        username_list = User.objects.filter("user_name")
        password_list = User.objects.filter("password")
        username = request.POST['user_name']
        password = request.POST['password']

        for i in username_list:
            if i == username:
                for j in password_list:
                    if j==password:
                        return "okay you are saladman"
                    else:
                        return "retry  enter your password"
                    
            
            else:
                return "retry your id and password please"
            
            
                    
        
        
        
        # authenticate방법 - 사용하지 x 예정
        # user = authenticate(request,user_name=username,password=password)


        if user is not None:
            okay= True
            return okay  #앵귤러에게 okay변수(TRUE) 보내기
        
        else:

            return okay #앵귤러에게 okay변수(FALSE) 보내기 
        





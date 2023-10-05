from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from .models import UserSignup
import urllib.request
import json


# Create your views here.



# 1. 회원가입
# user/signup
def signup(request):
  
  if request.method == 'POST':

    # POST처리 성공여부 확인
    print("success")

    # try:
 
    #어느 곳에 데이터가 들어가있는지 확인(body or POST)
    print('body',request.body)
    print('post',request.POST)


    #프론트에서 데이터 받아서 저장
    payload = json.loads(request.body)
    print("payload" , payload)
    username = payload["username"]
    password = payload["password"]


    print("test", username , password)

    # ---회원삭제---

    # deletes = UserSignup.objects.filter(id = '4')
    # deletess = deletes.delete()
   

    # 1. 회원가입시 user_name 중복체크

    # 1.1 현재 table의 username 모두 가져오기
    usernames = UserSignup.objects.all().values_list('user_name' , flat = True)
    print(usernames)
    
    # 1.2 중복체크 통과 -> 저장  , 불통 -> 경고메세지
    for i in usernames:
      if i == username:

        # 불통 -> 경고메세지 실행 및 http 오류 처리
        print("---error: 사용자 정보가 중복으로 존재합니다---")
        return HttpResponse("NotSupportService", status = 200)


    # 통과 -> 저장 및 확인메세지 출력
    new_user = UserSignup.objects.create(user_name= username , password =password )
    print("---success: 저장이 되었습니다---")
    return HttpResponse("GOOD SIGNUP" , status = 200)

    
       
        
    # except Exception as e:
    #   print("error", e)


        

   
   

      
    
      
    
    
    
    # return redirect('/api/signin')
  

# 2. 로그인
#POST. http://{host}/api/user/login & payload: {user_name: "USER_NAME", password: "PASSWORD" }

# def signin(request):
#   if request.method
# 쿠키 동작방식

#1. 클라이언트가 페이지 요청
#2. 서버에서 쿠키 생성
#3. HTTP 헤더에 쿠키를 포함시켜 응답
#4. 브라우저가 종료되어도 쿠키 만료 기간이 있다면 클라이언트(브라우저)에서 보관하고 있음
#5. 같은 요청을 할 경우 HTTP 헤더에 쿠키를 함께 보냄
#6. 서버에서 쿠키를 읽어 이전 상태 정보를 변경할 필요가 있을 떄 쿠키를 업데이트 하여 변경된 쿠키를 HTTP 헤더에 포함시켜 응답


# 쿠키 만들기

set_cookie("junjoy",10,max_age= None)

#name, value :필수 인자

request.COOKIE["junjoy"]

#쿠키 데이터를 읽으면 , 수가 아닌 문자열로 반환된다


# 로그인 

def login(request):
  # 해당 쿠키에 값이 없을 경우 None 을 리턴한다.
  if request.COOKIES.get('username') is not None:
    username = request.COOKIES.get('username')
    password = request.COOKIES.get('password')
    user = auth.authenticate(request, usernme = username, password = password)
    if user is not None:
      auth.login(request, user)
      return redirect("account:hone")
  
  elif request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(request, username = username, password = password)
    
    if user is not None:
      auth.login(request, user)
      if request.POST.get('keep_login')  == 'TRUE':
        response.set_cookie('username', username)
        response.set_cookie('password', password)
        return response
      return redirect("account:home")
    else:
      return render(request, 'account/login.html', {'error' : 'username or password is not incorrect'})
  
  else:
    return render(request, 'account/login.html')
  
  return render(request, 'account/login.html')



# 로그아웃

def logout(request):
  response = render(request, 'account/home.html')
  response.delete_cookie('username')
  response.delete_cookie('password')
  auth.logout(request)
  return response

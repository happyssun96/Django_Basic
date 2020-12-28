from django.shortcuts import render, redirect
from .models import Ouruser
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password # 장고의 자동 암호화 기능
from .forms import LoginForm

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None) # 앞에서 입력한 name필드에 있는 값을 key로 해서 전달
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None) # 딕셔너리 형태이기 때문에 key가 없으면 에러가남 -> get함수로 기본값을 None으로 지정
        re_password = request.POST.get('re-password', None) # 만약 key값이 없으면 기본값으로 None을 지정

        res_data = {} # 에러메시지를 담을 변수

        if not (username and useremail and password and re_password): # 빈 문자열이 있거나 모든 값들이 다 들어가지 않다면 에러 메시지 출력
            res_data['error'] = '모든 값을 입력해야 합니다.'
        elif password != re_password: # 비밀번호가 다를 때 에러 메시지 출력
            res_data['error'] = '비밀번호가 다릅니다...' # error라는 키와 문자열 넣음
        else:
            ouruser = Ouruser( # model에서 만든 ouruser를 가져와 생성
                username = username, # 클래스 변수를 객체하나 생성
                useremail = useremail,
                password = make_password(password)
            ) 
            ouruser.save() # 저장

        return render(request, 'home.html', res_data) # html코드로 res_data 전달

def login(request):
    if request.method =='POST': # POST일때와 아닐때를 구분
        form = LoginForm(request.POST) # POST 데이터를 넣어준다
        if form.is_valid(): # form에 있는 데이터가 정상적인지
            request.session['user'] = form.user_id # session에 form 안의 user_id를 넣는다
            return redirect('/') # 로그인에 성공하면 홈화면으로 간다
    else: 
        form = LoginForm() # 그렇지 않을때는 빈 객체로 넣음    
    return render(request, 'login.html', {'form' : form})

def home(request):
    
    return render(request, 'home.html') 

def logout(request):
    if request.session.get('user'): # user값이 있다면
        del(request.session['user']) # 삭제시킨다.
    return redirect('/') # 홈 화면으로 돌아온다.


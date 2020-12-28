from django import forms
from .models import Ouruser
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required' : '아이디를 입력해주세요'
        },
        max_length=32, label="사용자 이름") # 입력받을 아이디
    password = forms.CharField(
        error_messages={
            'required' : '비밀번호를 입력해주세요'
        },
        widget=forms.PasswordInput, label="비밀번호") # 입력받을 비밀번호

    def clean(self): 
        cleaned_data = super().clean() # 기존에 들어있던 clean()함수를 호출 -> 값이 들어있지 않다면 실패처리해준다
        username = cleaned_data.get('username') # 값이 들어있다는 검증이 끝나면 값을 가져온다
        password = cleaned_data.get('password')

        if username and password: # 각 값이 빈 값이 아닐때
            try:
                ouruser = Ouruser.objects.get(username = username) # 모델로부터 정보를 가져온다
            except Ouruser.DoesNotExist: # Ouruser 모델에서 가져온 username이 존재하지 않을 때
                self.add_error('username', '아이디가 없습니다...') # 에러 메시지 넣는다
                return

            if not check_password(password, ouruser.password): # 비밀번호가 다르면
                self.add_error('password', '비밀번호가 틀렸습니다...') # add_error()함수 -> 에러 메시지 넣는다
            else: # 비밀번호가 맞으면
                self.user_id = ouruser.id # user_id를 넣어준다
                # self를 통해 클래스 변수 안에 들어가므로 밖에서도 접근 가능

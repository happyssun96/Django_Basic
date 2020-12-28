from django.db import models

class Ouruser(models.Model): # 장고에서 제공하는 models.Model을 상속
    username = models.CharField(max_length=64, verbose_name='사용자명')
#이름을 담는 필드 , 최대 길이는 64, admin에서 관리자가 내릴 명령이 사용자명이라는 이름으로 보입니다
    useremail = models.EmailField(max_length=128, verbose_name='사용자이메일')
    #이메일 필드 추가
    password = models.CharField(max_length=64, verbose_name='비밀번호')
#비밀번호를 담는 필드  문자열 필드  
    registered_dttm = models.DateField(auto_now_add=True, verbose_name='등록시간')
#가입한 날짜를 담는 곳, 날짜와 시간을 표현, auto_now_add -> 클래스가 저장되는 시간이 자동으로 저장
#모델 클래스를 만들었는데 데이터베이스에 테이블명까지 지정할 수 있다.
    def __str__(self):
        return self.username # 맨 처음에 표시된 클래스 명을 문자열로 변환했을때의 값을 username 그 자체 그대로를 반환하도록 설정 

    class Meta:
        db_table = 'django_basic_ouruser'

    # 앱들과 구분하기위해 테이블명을 만듦
#모델을 관리할 관리자 페이지 활용


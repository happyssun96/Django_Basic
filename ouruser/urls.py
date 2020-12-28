from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
]
# 방금 만든 register를 등록하겠습니다. views.py에서 만든 함수를 불러오도록 연결한것입니다.
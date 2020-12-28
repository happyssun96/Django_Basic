from django.contrib import admin
from django.urls import path, include
from ouruser.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ouruser/', include('ouruser.urls')),
    path('', home),
    path('board/', include('board.urls'))
]

# user와 관련된 것들은 ouruser에 있는 urls를 사용하겠다
# ouruser 아래에 오는 url들은 ouruser 아래 url에서 관리 -> ouruser폴더 안에 urls.py 만듦
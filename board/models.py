from django.db import models

class Board(models.Model): 
    title = models.CharField(max_length=128, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('ouruser.Ouruser', on_delete=models.CASCADE, verbose_name='작성자') 
    # 데이터베이스를 이용해 연결 -> Ouruser 모델을 연결, CASCADE를 사용함으로써 사용자 정보가 삭제되었을 때 그 사용자의 모든 글들이 삭제된다.
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'django_board'




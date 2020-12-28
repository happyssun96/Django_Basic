from django.shortcuts import render, redirect
from ouruser.models import Ouruser
from .models import Board
from .forms import BoardForm
from django.http import Http404 # 404에러 발생
from django.core.paginator import Paginator # paginator 클래스 이용

def board_list(request):
    all_boards = Board.objects.all().order_by('-id') # 모든 게시글을 최신순으로 가져온다
    page = int(request.GET.get('p', 1)) # 페이지 번호를 GET형태로 받는다 -> p값으로, 없으면 첫번째 페이지로 지정
    paginator = Paginator(all_boards, 2) # 한 페이지당 게시글 2 개씩 나오도록 설정
    boards = paginator.get_page(page) # paginator를 통해 get_page를 해서 게시글 전달 
    return render(request, 'board_list.html', {'boards' : boards}) 
    # paginator를 통해서 가져왔기 때문에 boards안에 이미 페이지에 대한 정보가 들어있다.

def board_write(request):
    if not request.session.get('user'): 
        return redirect('/ouruser/login/') # 사용자가 없으면 로그인 페이지로 돌아간다

    if request.method == 'POST': # 로그인 처럼 method 확인
        form = BoardForm(request.POST)
        if form.is_valid(): # form에 있는 데이터가 정상적인지
            user_id = request.session.get('user') # 세션에서 user_id를 가져온다
            ouruser = Ouruser.objects.get(pk=user_id) # Ouruser모델에서 가져온다

            board = Board() # 클래스 변수 board 생성
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = ouruser # 사용자 정보는 세션을 활용
            board.save()
            return redirect('/board/list/') # 글 목록 페이지로 이동
    else:
        form = BoardForm()

    return render(request, 'board_write.html', {'form' : form})

def board_detail(request, pk): # 몇번째 글인지에 따라 pk 지정
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다')

    return render(request, 'board_detail.html', {'board' : board})


def board_update(request, pk):
    board = Board.objects.get(pk = pk)
    form = BoardForm(request.POST)

    if form.is_valid():
        board.title = form.cleaned_data['title']
        board.contents = form.cleaned_data['contents']
        board.save()
        return redirect('/board/list/')
    else:
        return render(request,'board_write.html',{'form' : form})

def board_delete(request, pk):
    board = Board.objects.get(pk = pk)
    board.delete()
    return redirect('/board/list/')
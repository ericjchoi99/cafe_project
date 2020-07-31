from django.shortcuts import render, get_object_or_404, redirect
from .models import Board
from user.models import CustomUser
# Create your views here.

def board_read(request):
    boards = Board.objects.all()
    context = {'boards': boards}
    return render(request, 'board/read.html', context)

def board_read_one(request, pk):
    board = get_object_or_404(Board, pk=pk) #첫번째 pk는 board안에있는 pk, 두번째 pk는 11번째 줄 pk에 대응
    context = {'board': board}
    return render(request, 'board/read_one.html', context)

def board_create(request):
    if request.method == 'POST' and request.session.get('user', False): #로그인해야 기능 이용 가능 
        title = request.POST['title']
        author = get_object_or_404(CustomUser, username = request.session['user'])
        content = request.POST['content']
        

        board = Board(
            author = author,
            title = title,
            content = content,
            

        )

        board.save()

        return redirect('board_read')
    else:
        return render(request, 'board/create.html')    
def board_update(request, pk): 
    title = request.POST['title']
    author = request.POST['author']
    Cuser = CustomUser.objects.get(username=author) #커스텀유저 안에서 author라는 이름을 가진 객체를 가져오는것 
    content = request.POST['content']
    board = Board.objects.get(pk=pk)
    board.title = title
    board.author = Cuser
    board.content = content
    board.save() 

    return redirect('board_read')
def pre_update(request, pk):
    board = Board.objects.get(pk=pk)
    context = {'board':board}
    return render(request, "board/update.html", context)

def board_delete(request, pk): 
    board = Board.objects.get(pk=pk)
    board.delete()
    return redirect('board_read')      
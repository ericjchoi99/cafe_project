from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import check_password
from .models import CustomUser
# Create your views here.

def sign_up(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['password']
        c_pwd = request.POST['check_password']

        if CustomUser.objects.filter(email=email).distinct():
            return render(request, "user/signUp.html", {"err" : "중복 아이디 존재"})

        if pwd != c_pwd :
            return render(request, "user/signUp.html", {"err" : "암호는 서로 일치해야 합니다."})

        customUser = CustomUser(   #customUser = 변수이름
            username = username,
            email = email,

        )
        customUser.set_password(pwd) #set_password : 암호화해서 저장해주는 함수(장고에서 제공)

        customUser.save()

        return redirect("home")
    else: 
        return render(request, "user/signUp.html")
    
def login(request):
    if request.method == "POST":
        email = request.POST['email']
        pwd = request.POST['password']

        user = get_object_or_404(CustomUser, email = email)

        if check_password(pwd, user.password):
            request.session['user'] = user.username
            return redirect('home')
        
        else:
            return render(request, "user/login.html", {"err": "패스워드가 틀렸습니다."})

    else:
        return render(request, 'user/login.html')

def logout(request):
    if request.session.get('user', False) :
        request.session.modified = True
        del request.session['user']
        return redirect("home")
    else:
        return redirect("home")
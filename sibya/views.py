from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from .models import Notice
from django.shortcuts import get_list_or_404

@login_required(login_url="login")
def index(request):
    return render(request, "index.html")

@login_required(login_url="login")
def all_notice(request):
    notices = get_list_or_404(Notice.objects.order_by("schedule"))
    return render(request, "all_notice.html", {"notices": notices})

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

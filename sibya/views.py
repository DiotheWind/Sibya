from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, NoticeForm, FeedbackForm
from .models import Notice, Organization
from django.db.models import Q
from django.shortcuts import get_object_or_404

@login_required(login_url="login")
def index(request):
    return render(request, "index.html")

@login_required(login_url="login")
def notice_dashboard(request):
    if not request.user.is_president:
        return redirect("index")

    notices = Notice.objects.filter(author=request.user).order_by("-schedule")

    return render(request, "notice_dashboard.html", {"notices": notices})

@login_required(login_url="login")
def all_notice(request):
    notices = Notice.objects.all() # start will all notices
    organizations = Organization.objects.all() # get all organizations for the filter dropdown

    # apply search filter
    search_query = request.GET.get("search", "")
    if search_query:
        notices = notices.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(organization__name__icontains=search_query)
        )

    # apply organization filter
    org_id = request.GET.get("organization", "")
    if org_id:
        notices = notices.filter(organization_id = org_id)

    # order by schedule
    notices = notices.order_by("schedule")

    context = {
        "notices": notices,
        "organizations": organizations,
        "search_query": search_query
    }

    return render(request, "all_notice.html", context)


@login_required(login_url="login")
def view_notice(request, id):
    notice = get_object_or_404(Notice, id=id)
    return render(request, "view_notice.html", {"notice": notice})

@login_required(login_url="login")
def add_notice(request):
    if not request.user.is_president:
        return redirect("index")

    if request.method == "POST":
        form = NoticeForm(request.POST)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.author = request.user
            notice.save()
            return redirect("all_notices")
    else:
        form = NoticeForm()
    return render(request, "add_notice.html", {"form": form})

@login_required(login_url="login")
def edit_notice(request, id):
    notice = get_object_or_404(Notice, id=id)

    if not request.user.is_president or notice.author != request.user:
        return redirect("index")

    if request.method == "POST":
        form = NoticeForm(request.POST, instance=notice)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = NoticeForm(instance=notice)

    return render(request, "add_notice.html", {
        "form": form,
        "edit": True
    })

@login_required(login_url="login")
def delete_notice(request, id):
    notice = get_object_or_404(Notice, id=id)
    if not request.user.is_president or notice.author != request.user:
        return redirect("index")

    if request.method == "POST":
        notice.delete()
        return redirect("index")

    return redirect("index")

@login_required
def join_notice(request, notice_id):
    notice = get_object_or_404(Notice, id=notice_id)
    notice.participants.add(request.user)

    return redirect("view_notice", id=notice_id)

@login_required
def leave_notice(request, notice_id):
    notice = get_object_or_404(Notice, id=notice_id)
    notice.participants.remove(request.user)

    return redirect("view_notice", id=notice_id)

@login_required
def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.author = request.user
            feedback.save()
            return redirect("all_notices")
    else:
        form = FeedbackForm()

    return render(request, "feedback_form.html", {"form": form})

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

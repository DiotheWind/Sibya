from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("notices/", views.all_notice, name="all_notices"),
    path("notices/<int:id>/", views.view_notice, name="view_notice"),
    path("add_notice/", views.add_notice, name="add_notice"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout")
]

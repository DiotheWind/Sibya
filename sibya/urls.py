from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("notices/", views.all_notice, name="all_notices"),
    path("notices/<int:id>/", views.view_notice, name="view_notice"),
    path("notices/<int:id>/edit/", views.edit_notice, name="edit_notice"),
    path("notices/<int:id>/delete/", views.delete_notice, name="delete_notice"),
    path("notice/<int:notice_id>/join/", views.join_notice, name="join_notice"),
    path('notice/<int:notice_id>/leave/', views.leave_notice, name='leave_notice'),
    path("add_notice/", views.add_notice, name="add_notice"),
    path("notice_dashboard/", views.notice_dashboard, name="notice_dashboard"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout")
]

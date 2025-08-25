from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    
    path("", views.home_view, name="home"),
    
    path("add/", views.add_student, name="add"),
    path("update/<int:student_id>/", views.update_marks, name="update"),
    path("delete/<int:student_id>/", views.delete_student, name="delete"),
]






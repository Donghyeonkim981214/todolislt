from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.log_out, name="logout"),
    path("signup/", views.UserCreateView.as_view(), name="signup"),
    path("profile/<int:pk>/", views.UserDetailView.as_view(), name="profile"),
    path("profile/update/", views.UserUpdateView.as_view(), name="profileupdate"),
    path("profile/password_update/", views.UserpasswordUpdateView.as_view(), name="passwordupdate"),
]
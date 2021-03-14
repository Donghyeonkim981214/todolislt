from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout

from . import models as user_models
from . import forms as user_forms

from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic import UpdateView, DetailView, FormView

from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import LoggedOutOnlyView, UserOnlyView


class UserLoginView(LoginView):
    """User Login View"""
    template_name = "users/login.html"

def log_out(request):
    logout(request)
    return redirect(reverse("home:home"))


class UserCreateView(LoggedOutOnlyView, FormView):

    template_name = "users/signup.html"
    form_class = user_forms.SignupForm
    success_url = reverse_lazy("user:login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class UserDetailView(LoginRequiredMixin, UserOnlyView, DetailView):
    login_url = '/users/login/'

    model = user_models.User
    context_object_name = "user_obj"   
    template_name = "users/profile.html"


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = user_models.User
    template_name = "users/profile_update.html"
    fields = (
        "first_name",
        "last_name",
        "email",
        "gender",
        "bio",
        "birthday",
    )

    def get_object(self, queryset=None):
        return self.request.user

class UserpasswordUpdateView(LoginRequiredMixin, PasswordChangeView):
    template_name = "users/password_update.html"
    success_url = reverse_lazy('user:login')
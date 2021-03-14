from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

class CreatorOnlyView(UserPassesTestMixin):
    def test_func(self):
        self.object = self.get_object()
        if self.object.created_by is None:
            return self.request
        return self.request.user == self.object.created_by

    def handle_no_permission(self):
        return redirect("home:home")

class LoggedOutOnlyView(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect("home:home")
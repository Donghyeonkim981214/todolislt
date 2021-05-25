from django.db import models
from users import models as user_models

from django.urls import reverse

# Create your models here.
class Todo(models.Model):
    """ Todo model """
    content = models.TextField()
    deadline = models.DateField(null = True, blank = True)
    posted_day = models.DateTimeField(auto_now_add = True)
    success = models.BooleanField(default = False)
    success_day = models.DateTimeField(null = True, blank = True)
    created_by = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null = True, blank = True)

    def get_absolute_url(self):
        return reverse("todo:detail", kwargs={"pk": self.pk})
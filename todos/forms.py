from django import forms
from . import models
import datetime

current_year = datetime.date.today().year
YEARS= [x for x in range(current_year,current_year+5)]

class TodoForm(forms.ModelForm):
    class Meta:
        model = models.Todo
        fields = (
            "content",
            "deadline",
        )
        widgets = {
            "deadline": forms.SelectDateWidget(years=YEARS),
        }

    def save(self):
        todo = super().save(commit=False)
        return todo
    
    def clean_deadline(self):
        deadline = self.cleaned_data['deadline']
        today = datetime.date.today()
        if deadline is not None and deadline < today:
             self.add_error("deadline", forms.ValidationError("Deadline must be more than today"))
        return deadline

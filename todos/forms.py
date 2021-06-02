from django import forms
from . import models
import datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, MultiWidgetField

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
        help_texts = { 'deadline': ('You can set a deadline if you need it.'), } 

    def save(self):
        todo = super().save(commit=False)
        return todo
    
    def clean_deadline(self):
        deadline = self.cleaned_data['deadline']
        today = datetime.date.today()
        if deadline is not None and deadline < today:
             self.add_error("deadline", forms.ValidationError("Deadline must be more than today"))
        return deadline

    def __init__(self, *args, **kwargs):
        self.create = kwargs.pop("create", False)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Create' if self.create else 'Update', css_class='btn-primary'))
        self.helper.layout = Layout(
            Row(
                Column('content', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                MultiWidgetField('deadline', attrs=({'style': 'width: 33%; display: inline-block;'})),
                css_class='form-row'
            ),
        )
        self.helper.label_class = 'd-block'

from django import forms
from . import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, MultiWidgetField, Fieldset

class SignupForm(forms.ModelForm):
    """User Sign up Form"""

    password = forms.CharField(widget=forms.PasswordInput)
    check_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = models.User
        fields = ("first_name", "last_name", "email", "username", "gender", "birthday")

    def clean_check_password(self):
        password = self.cleaned_data.get("password")
        check_password = self.cleaned_data.get("check_password")
        if password != check_password:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password

    def save(self):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")
        user.set_password(password)
        user.save()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset("Who are you?", "first_name", "last_name", "email", "username", "password", "check_password", "gender", "birthday"),
            Submit('submit', 'Register')
        )
        self.helper.label_class = 'd-block'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = (
            "first_name",
            "last_name",
            "email",
            "gender",
            "bio",
            "birthday",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                "Your Profile",
                "first_name",
                "last_name",
                "email",
                "gender",
                "birthday",
                "bio",
            ),
            Submit('submit', 'Profile update')
        )
        self.helper.label_class = 'd-block'

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms.renderers import TemplatesSetting

from accounts.constants import HELP_TEXT, MESSAGES

User = get_user_model()

FORM_TEMPLATE = "accounts/form.html"


class RegisterForm(UserCreationForm):
    renderer = TemplatesSetting()

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )

    template_name = FORM_TEMPLATE

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].help_text = HELP_TEXT["password"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(MESSAGES["email"], code="invalid")

        return email

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(MESSAGES["username"], code="invalid")

        return username

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data is not None:
            password1 = cleaned_data.get("password1")
            password2 = cleaned_data.get("password2")

            if password1 and password2 and password1 != password2:
                raise forms.ValidationError(
                    MESSAGES["password_not_match"], code="invalid"
                )

        return cleaned_data

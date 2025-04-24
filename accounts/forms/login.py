from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.forms.renderers import TemplatesSetting

from accounts.constants import MESSAGES

User = get_user_model()

FORM_TEMPLATE = "accounts/form.html"


class LoginForm(forms.Form):
    renderer = TemplatesSetting()

    username = forms.CharField(
        required=True,
        widget=forms.TextInput(),
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
    )

    template_name = FORM_TEMPLATE

    def __init__(self, *args, **kwargs):
        self.user = None
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data is not None:
            username = cleaned_data.get("username")
            password = cleaned_data.get("password")

            if username and password:
                user = authenticate(username=username, password=password)

                if user is None:
                    raise forms.ValidationError(
                        MESSAGES["invalid_username_or_password"], code="invalid"
                    )

                self.user = user

        return cleaned_data

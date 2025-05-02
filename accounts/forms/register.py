from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms.renderers import TemplatesSetting

from accounts.constants import HELP_TEXT, MESSAGES

User = get_user_model()

FORM_TEMPLATE = "accounts/form.html"


class RegisterForm(UserCreationForm):
    renderer = TemplatesSetting()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    template_name = FORM_TEMPLATE

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].error_messages["unique"] = MESSAGES["username"]

        self.fields["email"].error_messages["unique"] = MESSAGES["email"]

        self.fields["password1"].help_text = HELP_TEXT["password"]

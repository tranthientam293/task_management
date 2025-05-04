from django.contrib.auth import get_user_model, forms
from django.forms.renderers import TemplatesSetting

User = get_user_model()


class LoginForm(forms.AuthenticationForm):
    renderer = TemplatesSetting()

    class Meta:
        model = User
        fields = ["username", "password"]

    template_name = "accounts/form.html"

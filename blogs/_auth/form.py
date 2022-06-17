from django.forms import models
from django.contrib.auth.models import User

class SignUpForm(models.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ("username", "email", "password", "first_name", "last_name")

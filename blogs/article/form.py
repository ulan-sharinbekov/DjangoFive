from django import forms
from .models import *

class CreateArticle(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Article
        # fields = '__all__'
        fields = ("title", "content", "category_id", "image", "author_id")

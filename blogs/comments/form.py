from django.forms import ModelForm

from .models import Comment

class CreateComment(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Comment
        # fields = '__all__'
        fields = ("description", "author_id")

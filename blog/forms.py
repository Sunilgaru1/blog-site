from django.forms import ModelForm
from .models  import BlogModel,Comment

class BlogForm(ModelForm):

    class Meta:
        model = BlogModel
        fields = ['title','content']

class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['content']
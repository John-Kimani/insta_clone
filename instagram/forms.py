from django import forms
from .models import Post, Comments

class UploadForm(forms.ModelForm):
    '''
    Class that handles forms
    '''
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ["likes", "date", "comments"]

class CommentForm(forms.ModelForm):
    '''
    Class that handles comments
    '''
    class Meta:
        model = Comments
        fields = "__all__"
        exclude = ["pub_date"]

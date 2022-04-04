from django import forms
from .models import Post

class UploadForm(forms.ModelForm):
    '''
    Class that handles forms
    '''
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ["likes", "date", "comments"]

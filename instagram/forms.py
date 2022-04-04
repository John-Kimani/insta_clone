from django import forms
from .models import Photos

class UploadForm(forms.ModelForm):
    '''
    Class that handles forms
    '''
    class Meta:
        model = Photos
        fields = "__all__"
        excude = {"likes"}

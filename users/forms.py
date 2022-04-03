from cProfile import label
from django import forms

class LoginForm(forms.Form):
    '''
    Class that handles user login
    '''
    username = forms.CharField(label='username', max_length=30)
    password = forms.PasswordInput()
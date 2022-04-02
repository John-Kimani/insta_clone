from django.shortcuts import render

# Create your views here.

def index(request):
    '''
    Function for welcome page
    '''
    return render(request, 'index.html')
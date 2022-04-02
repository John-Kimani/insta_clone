from django.shortcuts import render
from .models import Photos

# Create your views here.

def index(request):
    '''
    Function for welcome page
    '''
    images = Photos.objects.all()

    return render(request, 'timeline.html', {"images":images})
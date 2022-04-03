from django.shortcuts import render
from .models import Photos

# Create your views here.

def index(request):
    '''
    View function for the timeline page
    '''
    images = Photos.objects.all()

    return render(request, 'timeline.html', {"images":images})

def profile_page(request):
    '''
    View function for users profile page
    '''
    images = Photos.objects.all()
    return render(request, 'profile.html', {"images":images})
from django.shortcuts import render
from .models import Photos
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def index(request):
    '''
    View function for the timeline page
    '''
    # images = Photos.objects.all()
    caption = Photos.display_all()
    return render(request, 'timeline.html', {"captions":caption})

def profile_page(request):
    '''
    View function for users profile page
    '''
    images = Photos.objects.all()
    return render(request, 'profile.html', {"images":images})
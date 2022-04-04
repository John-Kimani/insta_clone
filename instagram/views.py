from django.shortcuts import redirect, render
from .models import Photos, Profile
from django.contrib.auth.decorators import login_required
from .forms import UploadForm


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
    profile = Profile.display_profile()
    return render(request, 'profile.html', {"images":images, "profiles":profile})


def post_items(request):
    '''
    View function that enables users to make posts
    '''
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('instagram')
    else:
        form = UploadForm()
        
    caption = Photos.display_all()
    return render(request, 'create_posts.html', {"posts":caption, "form": form})
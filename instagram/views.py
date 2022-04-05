from django.shortcuts import redirect, render
from .models import Photos, Profile, Post, Comments
from django.contrib.auth.decorators import login_required
from .forms import UploadForm, CommentForm
from django.contrib.auth import logout


def welcome(request):
    
    return render(request, "welcome.html")

@login_required(login_url='/accounts/login/')
def index(request):
    '''
    View function for the timeline page
    '''
    # images = Photos.objects.all()
    caption = Photos.display_all()
    post = Post.display_posts()
    profile = Profile.display_profile()
    return render(request, 'timeline.html', {"captions":caption, "posts":post, "profiles":profile})

@login_required(login_url='/accounts/login/')
def profile_page(request):
    '''
    View function for users profile page
    '''
    images = Photos.objects.all()
    profile = Profile.display_profile()
    
    form = CommentForm
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = Comments()
            new_comment.message = form.cleaned_data['comment']
            new_comment.save()
        return redirect('profile')  

    return render(request, 'profile.html', {"images":images, "profiles":profile, "form": form})

@login_required(login_url='/accounts/login/')
def post_items(request):
    '''
    View function that enables users to make posts
    '''
    form = UploadForm
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post()
            post.title = form.cleaned_data['title']
            post.image = form.cleaned_data['image']
            post.caption = form.cleaned_data['caption']
            post.save()
        return redirect('instagram')
    
    return render(request, 'create_posts.html', {"form": form})

def logout_current_user(request):

    return render(request, "logout.html")
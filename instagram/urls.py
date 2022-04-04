from django.urls import path
from . import views


urlpatterns =  [
    path('', views.index, name='instagram'),
    path('profile/', views.profile_page, name='profile'),
    path('post/', views.post_items, name='post'),
    path('logout/', views.logout_current_user, name='logout'),
]
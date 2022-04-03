from django.urls import path
from . import views


urlpatterns =  [
    path('', views.index, name='instagram'),
    path('profile/', views.profile_page, name='profile'),
]
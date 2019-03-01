from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    # path('', views.post_list, name='post_list'),
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('contact', views.contact, name='contact'),
    path('classes', views.classes, name='classes'),
    path('fighters', views.fighters, name='fighters'),
    path('profile/<int:pk>/', views.profile_detail, name='profile_detail'),
    path('sponsor', views.sponsor, name='sponsor'),
    path('news', views.news, name='news'),
    path('about', views.about, name='about'),




]

from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post, Profile, Event, GalleryPhoto, Coach
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.


def news(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/news.html', {'posts': posts})


def sponsor(request):
    return render(request, 'blog/sponsor.html')


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')


def classes(request):
    return render(request, 'blog/classes.html')


def landing(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/index.html', {'posts': posts})


def fighters(request):
    profiles = Profile.objects.filter(
        published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/fighters.html', {'profiles': profiles})


def coaches(request):
    coaches = Coach.objects.filter(
        published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/coaches.html', {'coaches': coaches})


def coach_profile(request, pk):
    coach = get_object_or_404(Coach, pk=pk)
    return render(request, 'blog/coach_profile.html', {'coach': coach})


def gallery(request):
    galleryPhotos = GalleryPhoto.objects.filter(
        published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/gallery.html', {'galleryPhotos': galleryPhotos})


def profile_detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    return render(request, 'blog/fighter_profile.html', {'profile': profile})


def index(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('-published_date')
    events = Event.objects.filter(
        published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/index.html', {'posts': posts, 'events': events})

# def index(request):
#     events = Event.objects.filter(
#         published_date__lte=timezone.now()).order_by('-published_date')
#     return render(request, 'blog/index.html', {'events': events})


def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

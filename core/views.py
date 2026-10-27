from django.shortcuts import render
from blog.models import Post

def blog(request):
    posts = Post.objects.all()
    return render(request, 'core/blog.html', {'posts': posts})

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def store(request):
    return render(request, 'core/store.html')

from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Blog

def home(request):
    return render(request, 'myprofile/home.html')

def about(request):
    return render(request, 'myprofile/about.html')

def resume(request):
    return render(request, 'myprofile/resume.html')

def portfolio(request):
    return render(request, 'myprofile/portfolio.html')

def services(request):
    return render(request, 'myprofile/services.html')

def blog(request):
    posts = Blog.objects.all()  # Fetch all blog posts
    return render(request, 'myprofile/blog.html', {'posts': posts})

def blog_detail(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    return render(request, 'myprofile/blog-detail.html', {'post': post})


def testimonials(request):
    return render(request, 'myprofile/testimonials.html')

def contact(request):
    return render(request, 'myprofile/contact.html')

def portfolio_details(request):
    return render(request, 'myprofile/portfolio-details.html')



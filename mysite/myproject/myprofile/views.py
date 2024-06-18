from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.contrib import messages
from .forms import EmailPostForm, ContactForm
import logging
from .models import Blog
from django.urls import reverse
from django.http import HttpResponse
from django.template.loader import render_to_string

logger = logging.getLogger(__name__)

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

def blog_list(request):
    posts = Blog.objects.all()
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page', 1)
    try:
        posts_1 = paginator.page(page_number)
    except PageNotAnInteger:
        posts_1 = paginator.page(1)
    except EmptyPage:
        posts_1 = paginator.page(paginator.num_pages)
    return render(request, 'myprofile/blog.html', {'posts': posts_1})

def blog_detail(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    return render(request, 'myprofile/blog-detail.html', {'post': post})

def testimonials(request):
    return render(request, 'myprofile/testimonials.html')

def portfolio_details(request):
    return render(request, 'myprofile/portfolio-details.html')

def contact(request):
    return render(request, 'myprofile/contact.html')


def post_share(request, post_id):
    post_1 = get_object_or_404(Blog, pk=post_id)
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post_1.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post_1.title}"
            message = f"Read {post_1.title} at {post_url}\n\n{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, settings.EMAIL_HOST_USER, [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'myprofile/post_share.html', {'form': form, 'post': post_1, 'sent': sent})





def thank_you(request):
    return render(request, 'myprofile/thank_you.html')




logger = logging.getLogger(__name__)

def submit_form_1(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"From: {name}\nEmail: {email}\n\n{message}"

        try:
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                ['kessellyalton1@gmail.com'],
                fail_silently=False,
            )
            return redirect('thank_you')
        except Exception as e:
            logger.error(f"Error sending email: {e}")
            return render(request, 'contact.html', {'error_message': 'There was an error sending your email. Please try again later.'})

    return render(request, 'contact.html')

from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.http import FileResponse
from .forms import EmailPostForm, ContactForm, UploadFileForm
from .models import Blog, Resume
import logging
import os
from django.http import HttpResponse, HttpResponseRedirect

logger = logging.getLogger(__name__)

def resume_view(request):
    return render(request, 'myprofile/resume.html')


def upload_resume(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')
    else:
        form = UploadFileForm()
    return render(request, 'myprofile/upload.html', {'form': form})


def download_resume(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'uploads/resume.pdf')

    if not os.path.exists(file_path):
        logger.error(f"File not found: {file_path}")
        return HttpResponse("File not found", status=404)

    try:
        return FileResponse(open(file_path, 'rb'), as_attachment=True, content_type='application/pdf')
    except Exception as e:
        logger.error(f"Error opening file: {e}")
        return HttpResponse("Error opening file", status=500)


def upload_success(request):
    return render(request, 'myprofile/upload_success.html')


def home(request):
    return render(request, 'myprofile/home.html')


def about(request):
    return render(request, 'myprofile/about.html')


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
            return render(request, 'myprofile/contact.html',
                          {'error_message': 'There was an error sending your email. Please try again later.'})

    return render(request, 'myprofile/contact.html')

from django.shortcuts import render

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
    return render(request, 'myprofile/blog.html')

def testimonials(request):
    return render(request, 'myprofile/testimonials.html')

def contact(request):
    return render(request, 'yprofilen/contact.html')

def portfolio_details(request):
    return render(request, 'myprofile/portfolio-details.html')



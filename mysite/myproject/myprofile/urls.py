# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog_list, name='blog'),
    path('blog/<int:pk>/', views.blog_detail, name='blog-detail'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('portfolio-details/', views.portfolio_details, name='portfolio-details'),
    path('contact/', views.contact, name='contact'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('submit_form_1/', views.submit_form_1, name='submit_form_1'),
    path('thank_you/', views.thank_you, name='thank_you'),
]

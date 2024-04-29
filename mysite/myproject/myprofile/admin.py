from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date_posted', 'image']

admin.site.register(Blog, BlogAdmin)



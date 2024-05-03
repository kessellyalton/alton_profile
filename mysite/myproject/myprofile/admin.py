from django.contrib import admin
from django import forms
from .models import Blog
from django_ckeditor_5.widgets import CKEditor5Widget

# Define a ModelForm for the Blog model using CKEditor5 for the 'content' field
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'  # Include all fields from the Blog model
        widgets = {
            'content': CKEditor5Widget(),  # Use CKEditor5Widget for the 'content' field
        }

# Customize the admin interface for the Blog model
class BlogAdmin(admin.ModelAdmin):
    form = BlogForm  # Use the custom form with CKEditor5Widget for the 'content' field
    list_display = ['title', 'author', 'date_posted', 'image']  # Set the fields to display in the list view

# Register the Blog model with the customized admin interface
admin.site.register(Blog, BlogAdmin)

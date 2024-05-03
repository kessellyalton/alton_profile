from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
import bleach

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = CKEditor5Field('Content')
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)  # Optional image field

    def save(self, *args, **kwargs):
        self.content = bleach.clean(self.content, tags=['p', 'strong', 'em', 'a'], attributes={'a': ['href', 'title']},
                                    strip=True)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title


from django.db import models
from django.shortcuts import reverse

class Post(models.Model):
    title = models.CharField(max_length = 128)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('journal:post_detail', args=[self.pk])



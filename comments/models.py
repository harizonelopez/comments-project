from django.db import models
from django.utils import timezone
from django.urls import reverse

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'Comment on {self.post.title}'

class Post(models.Model):
    title = models.CharField(max_length=50)
    caption = models.TextField()

    def __str__(self):
        return f'Post- {self.title}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'id': self.id})

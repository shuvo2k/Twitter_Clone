from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    message = models.CharField(max_length=280)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def __str__(self):
        return self.message


class Comment(models.Model): 
    comment = models.CharField(max_length=150)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )

    def get_absolute_url(self):
        return reverse('post_list')
    
    def __str__(self):
        return self.comment

        
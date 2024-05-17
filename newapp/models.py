from audioop import reverse

from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User


class News(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    year = models.IntegerField()
    image = models.ImageField(upload_to='')


    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="55" height="55"/>' % self.image)

    def get_absolute_url(self):
        return reverse('User-Posts-Details', kwargs={'pk': self.pk})


class Comment(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=500)

    def __str__(self):
        return f"User: {self.user.username}"


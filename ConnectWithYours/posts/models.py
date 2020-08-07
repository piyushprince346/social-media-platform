from django.db import models
from django.urls import reverse
from django.conf import settings

import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

from groups.models import Group

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name='posts')
    created_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    content_html = models.TextField(editable=False)
    group = models.ForeignKey(Group,on_delete = models.CASCADE,related_name='posts')

    def __str__(self):
        return self.content

    def save(self,*args,**kwargs):
        self.content_html = misaka.html(self.content)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("posts:post_details", kwargs={
                                              "pk" : self.pk})

    class Meta:
        ordering = ['-created_on']
        unique_together = ['user','content']
    
    

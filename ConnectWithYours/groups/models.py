from django.db import models
from django.utils.text import slugify # it will connect a gap separeated strings with a hyphen
from django.contrib.auth import get_user_model
from django.urls import reverse

import misaka
# Create your models here.

from django import template
register = template.Library()

User = get_user_model() # returns  the user model which is active in this project
class Group(models.Model):
    name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    description = models.TextField()
    description_html = models.TextField(editable=False,blank=True,default='')
    members = models.ManyToManyField(User,through='GroupMember')

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('groups:group_details', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['name']
    
    

    
    

class GroupMember(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name='group_user')
    group = models.ForeignKey(Group,on_delete = models.CASCADE,related_name='membership')

    def __str__(self):
        return self.user.username
    
    class Meta:
        unique_together = ('group','user')
    

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    profile_pic = models.ImageField(default = 'default.png', upload_to = 'profile_pics')


    def __str__(self):
        return "@{}".format(self.user.username) # string reprentation of user will be like @piyush
    
from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    bio = models.TextField()
    avatar = models.ImageField(upload_to='avatars/')

    def __str__(self):
        return self.username

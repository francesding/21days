from django.db import models
from django.contrib.auth.models import User

class NewsFeedPost(models.Model):
    message = models.CharField(max_length=2048)
    user = models.ForeignKey(User)
    timestamp = models.DateField(auto_now_add=True)
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Travel(models.Model):
    country_name = models.CharField(max_length=128)
    body = models.TextField()
    img = models.ImageField(upload_to='media')
    created_at = models.DateTimeField(auto_now_add=True)

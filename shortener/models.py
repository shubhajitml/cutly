from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ShortURL(models.Model):
    original_url = models.URLField(blank=False)
    short_query = models.CharField(blank=False, max_length=8)
    visits_count = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

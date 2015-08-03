from django.db import models
from django.contrib.auth.models import User

class Twisser(models.Model):
    user = models.OneToOneField(User)
    nationality = models.CharField(max_length=50)
    twissies = models.IntegerField()


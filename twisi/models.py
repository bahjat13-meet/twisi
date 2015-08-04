from django.db import models
from django.contrib.auth.models import User


class Twisser(models.Model):
    user = models.OneToOneField(User)
    nationality = models.CharField(max_length=50)
    twissies = models.IntegerField(default=0)

class Drawing(models.Model):
	user = models.ForeignKey(User)
	filename = models.CharField(max_length=100)
	score = models.IntegerField(default=0)
	category = models.CharField(max_length=20)
	is_public = models.BooleanField(default=False)
	date = models.DateTimeField()
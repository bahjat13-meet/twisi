from django.db import models
from django.contrib.auth.models import User


class Twisser(models.Model):
    user = models.OneToOneField(User)
    nationality = models.CharField(max_length=50)
    twissies = models.IntegerField(default=0)

class Drawing(models.Model):
	twisser = models.ForeignKey(Twisser)
	filename = models.CharField(max_length=100)
	score = models.IntegerField(default=0)
	category = models.CharField(max_length=20)
	is_public = models.BooleanField(default=False)
	date = models.DateTimeField()

	def serialize(self):
		d = {
			'twisser_id': self.twisser.id,
			'filename' : self.filename,
			'score' : self.score,
			'category' : self.category,
			'is_public' : self.is_public,
			'date' : self.date 
			'drawing_id' : self.id
		} 
		return d

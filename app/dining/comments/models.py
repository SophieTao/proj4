from django.db import models
# from django.conf import settings

# Create your models here.
class comment(models.Model):
	description = models.CharField(max_length=300)
	feedback = models.CharField(max_length=300)

	def __str__(self):
		return self.description

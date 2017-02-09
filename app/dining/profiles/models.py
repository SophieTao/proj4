from django.db import models
from django.conf import settings
# Create your models here.
class profile(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

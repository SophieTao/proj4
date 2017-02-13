from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Cafe(models.Model):
	name = models.CharField(max_length=100,null=True)
	location = models.CharField(max_length=50,null=True)
	date = models.DateTimeField(null=True)
	description = models.CharField(max_length = 1000,null=True)
	Calories = models.PositiveIntegerField(null = True)

	def __str__(self):
		return self.name

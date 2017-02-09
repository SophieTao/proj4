from django.db import models
from django.conf import settings
import datetime
# Create your models here.
class cafe(models.Model):
	name = models.CharField(max_length=100)
	#location = models.CharField(max_length=50)
	#date = models.DateField(default=datetime.date.today)

	def __str__(self):
		return self.name

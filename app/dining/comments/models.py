from django.db import models
from django.core.urlresolvers import reverse
from profiles import models as profile_models
from cafes import models as cafe_models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Comment(models.Model):
	description = models.CharField(max_length=1300)
	feedback = models.CharField(max_length=300)
	author = models.ForeignKey(profile_models.Profile, null=True)
	date_written = models.DateTimeField(null=True)
	rating = models.PositiveIntegerField(null=True,validators=[MinValueValidator(1), MaxValueValidator(5),])
	meal = models.ForeignKey(cafe_models.Cafe, null=True)

	def __str__(self):
		return self.description

	def get_absolute_url(self):
		return reverse('comment-update', kwargs={'pk': self.pk})

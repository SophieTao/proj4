from django.contrib import admin
from .models import Profile

class profileAdmin(admin.ModelAdmin):
	class Meta:
		model=Profile

admin.site.register(Profile, profileAdmin)	



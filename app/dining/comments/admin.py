from django.contrib import admin
from .models import comment

class commentAdmin(admin.ModelAdmin):
	class Meta:
		model=comment

admin.site.register(comment, commentAdmin)	



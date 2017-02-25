from django.contrib import admin
from .models import Cafe

class CafeAdmin(admin.ModelAdmin):
	class Meta:
		model=Cafe

admin.site.register(Cafe, CafeAdmin)	



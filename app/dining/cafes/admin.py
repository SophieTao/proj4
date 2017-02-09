from django.contrib import admin
from .models import cafe

class cafeAdmin(admin.ModelAdmin):
	class Meta:
		model=cafe

admin.site.register(cafe, cafeAdmin)	



from django.contrib import admin
from .models import Company, Location


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'location')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Location, LocationAdmin)

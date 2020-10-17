from django.contrib import admin
from .models import Company, Location, Status


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'location')


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Status, StatusAdmin)

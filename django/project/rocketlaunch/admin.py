from django.contrib import admin
from .models import Company, Location, Status, Launch


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'location')


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')


class LaunchAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'cost',
        'time_date',
        'company',
        'status',
        'location',
    )


admin.site.register(Company, CompanyAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Launch, LaunchAdmin)

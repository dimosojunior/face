from django.contrib import admin
from MyApp.models import *

# Register your models here.
class RecordsAdmin(admin.ModelAdmin):
	list_display =["criminals","recorded_at","updated_at"]
	list_filter = ["recorded_at", "updated_at"]
	search_fields = ["criminals"]
class ActivitiesAdmin(admin.ModelAdmin):
	list_display =["activity_name", "link","recorded_at","updated_at"]
	list_filter = ["recorded_at", "updated_at"]
	search_fields = ["activity_name","link"]
class CriminalsAdmin(admin.ModelAdmin):
	list_display =["name","gender", "residence","recorded_at","updated_at"]
	list_filter = ["recorded_at", "updated_at"]
	search_fields = ["name", "residence"]

admin.site.register(Records, RecordsAdmin)
admin.site.register(Activities, ActivitiesAdmin)
admin.site.register(Criminals, CriminalsAdmin)

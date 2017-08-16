from django.contrib import admin
from sign.models import Event,User
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ['id','name','status','address','start_time']
    search_fields = ['name','start_time']
    list_filter = ['status']
admin.site.register(Event,EventAdmin)
admin.site.register(User)

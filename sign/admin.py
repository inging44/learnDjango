from django.contrib import admin
from sign import models
# Register your models here.
# add model table here so that we can add&edit data at admin page
admin.site.register(models.News)
admin.site.register(models.NewsDetail)
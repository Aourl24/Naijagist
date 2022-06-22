from django.contrib import admin
from django.db import models
from . import  models
# Register your models here.
#class titleAdmin(admin.ModelAdmin):
#    list_display=('category')


class commentAdmin(admin.StackedInline):
    model=models.Image

class titleAdmin(admin.ModelAdmin):
    list_display = ('head', 'category', 'Date')
    prepopulated_fields={'slug':('head',)}
    inlines=[commentAdmin]
    

admin.site.register(models.title, titleAdmin)
admin.site.register(models.Comment)
admin.site.register(models.Image)
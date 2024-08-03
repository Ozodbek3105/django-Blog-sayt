from pydoc import classname
from re import S
from django.contrib import admin
from django.http import HttpRequest

from settingapp.models import About, Social_links

class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request: HttpRequest) -> bool:
        return About.objects.all().count() == 0
                 
# Register your models here.
admin.site.register(About,AboutAdmin)
admin.site.register(Social_links)
from django.contrib import admin
from django.utils.safestring import mark_safe

from applications.help.models import *


@admin.register(Help)
class HelpAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')


@admin.register(Image)
class HelpImageAdmin(admin.ModelAdmin):
    list_display = ('get_image',)

    def get_image(self, object):
        if object.image:
            return mark_safe(f"<img src={object.image.url} width=250 height=300>")

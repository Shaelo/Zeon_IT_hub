from django.contrib import admin

from applications.footer.models import *


@admin.register(FirstFooterTab)
class FirstAdmin(admin.ModelAdmin):
    list_display = ('info', 'phone_num', 'icon')


@admin.register(SecondFooterTab)
class SecondAdmin(admin.ModelAdmin):
    list_display = ('messenger', 'url_or_phone')

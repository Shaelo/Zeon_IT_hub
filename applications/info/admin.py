from django.contrib import admin
from django.utils.safestring import mark_safe
from applications.info.forms import *
from applications.info.models import *


class ImageInAdmin(admin.TabularInline):
    model = Image
    fields = ('image',)
    max_num = 3


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    inlines = [ImageInAdmin]
    form = AboutUsAdminForm
    list_display = ('title', 'text')


@admin.register(Advantage)
class Advantage(admin.ModelAdmin):
    list_display = ('title', 'text', 'icon')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('title', 'text', 'get_image')

    def get_image(self, object):
        if object.image:
            return mark_safe(f"<img src={object.image.url} width=250 height=300>")


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    form = OfferAdminForm
    list_display = ('title', 'text')

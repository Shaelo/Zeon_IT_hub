from django.contrib import admin
from applications.product.forms import ProductAdminForm
from applications.product.models import Product, Image, Collection
from django.contrib.auth.models import *
from django.utils.safestring import mark_safe


class ImageInAdmin(admin.TabularInline):
    model = Image
    fields = ('image', 'color',)
    max_num = 8


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image')

    def get_image(self, object):
        if object.img:
            return mark_safe(f"<img src={object.img.url} width 250 height=300>")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInAdmin]
    form = ProductAdminForm
    list_display = (
        'collection',
        'name',
        'article',
        'price',
        'sale',
        'total_price',
        'text',
        'size',
        'amount_size',
        'cloth',
        'material',
    )


admin.site.site_header = 'Zeon shop!'
admin.site.unregister(Group)
admin.site.unregister(User)

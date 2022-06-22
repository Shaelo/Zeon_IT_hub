from applications.product.models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.gis import forms


class ProductAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = (
            'collection',
            'name',
            'article',
            'price',
            'sale',
            'text',
            'size',
            'cloth',
            'material',
        )

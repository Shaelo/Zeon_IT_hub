from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.gis import forms
from applications.info.models import *


class AboutUsAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = AboutUs
        fields = '__all__'


class NewsAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class OfferAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        models = Offer
        fields = '__all__'

from rest_framework import serializers
from applications.info.models import *


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ('title', 'text',)


class AboutUsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image',)


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('title', 'text',)


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('image', 'title', 'text')

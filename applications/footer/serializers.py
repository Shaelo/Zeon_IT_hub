from rest_framework import serializers
from applications.footer.models import FirstFooterTab, SecondFooterTab


class FirstFooterTabSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstFooterTab
        fields = ('phone_num', 'icon', 'info')


class SecondFooterTabSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondFooterTab
        fields = ('messenger', 'url_or_phone')

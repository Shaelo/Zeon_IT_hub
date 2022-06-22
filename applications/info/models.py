from django.core.validators import FileExtensionValidator
from django.db import models


class Advantage(models.Model):
    icon = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['svg', 'png'], message='Неправильный формат!')])
    title = models.CharField(max_length=255)
    text = models.TextField()


class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()


class Image(models.Model):
    image = models.ImageField(upload_to='images')
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name='images')


class News(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    text = models.TextField()


class Offer(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

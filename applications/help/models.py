from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='images')


class Help(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question



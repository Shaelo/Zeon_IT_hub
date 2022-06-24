from django.db import models
from colorfield.fields import ColorField
from django.core.exceptions import ValidationError


class Collection(models.Model):
    title = models.CharField(max_length=255, unique=True)
    img = models.ImageField()

    def __str__(self):
        return self.title


def even_number(size):
    if int(size[0:2]) % 2 != 0 or int(size[3:5]) % 2 != 0:
        raise ValidationError('Только четные числа!')


class Product(models.Model):
    collection = models.ForeignKey(Collection, related_name='product', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    article = models.CharField(max_length=255)
    price = models.IntegerField()
    sale = models.DecimalField(max_digits=3, decimal_places=1, default=0, blank=True, null=True)
    total_price = models.IntegerField(blank=True, null=True)
    text = models.TextField()
    size = models.CharField(max_length=5, validators=[even_number])
    cloth = models.CharField(max_length=255)
    amount_size = models.IntegerField(default=0, blank=True, null=True)
    material = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        discount = self.sale

        if discount > 0:
            discount_price = (self.price*discount)/100
            self.total_price = self.price - discount_price
            size = self.size
            self.amount_size = ((int(size[3:5]) - int(size[0:2])) / 2) + 1
        else:
            self.total_price = self.price
        super(Product, self).save(*args, **kwargs)


class Image(models.Model):
    image = models.ImageField(upload_to='images')
    color = ColorField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

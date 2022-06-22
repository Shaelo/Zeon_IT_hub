# Generated by Django 4.0.5 on 2022-06-22 10:59

import applications.product.models
import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('article', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('sale', models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=3, null=True)),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True)),
                ('text', models.TextField()),
                ('size', models.CharField(max_length=5, validators=[applications.product.models.even_number])),
                ('cloth', models.CharField(max_length=255)),
                ('amount_size', models.IntegerField(blank=True, default=0, null=True)),
                ('material', models.CharField(max_length=255)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.collection')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=None)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.product')),
            ],
        ),
    ]

# Generated by Django 5.0.1 on 2024-07-22 13:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0029_remove_product_productcategory_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('categoryId', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('categoryName', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colorName', models.CharField(max_length=25)),
                ('hexValue', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='size',
            fields=[
                ('sizeId', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('sizeName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('productId', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('productName', models.CharField(max_length=15)),
                ('discountPrice', models.FloatField()),
                ('productPrice', models.FloatField()),
                ('productImg', models.ImageField(upload_to='shopDtails')),
                ('productDetail', models.TextField()),
                ('productDesc', models.TextField()),
                ('productInfo', models.TextField()),
                ('productMaterial', models.TextField()),
                ('productCategory', models.ManyToManyField(related_name='productCategory', to='app.category')),
                ('productColor', models.ManyToManyField(related_name='productColor', to='app.color')),
                ('productSize', models.ManyToManyField(related_name='productSize', to='app.size')),
            ],
        ),
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productImage', models.ImageField(upload_to='shopDetails')),
                ('productColor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app.product')),
            ],
        ),
    ]

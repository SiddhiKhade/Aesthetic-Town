# Generated by Django 4.0.1 on 2022-04-05 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_productid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='productId',
        ),
    ]
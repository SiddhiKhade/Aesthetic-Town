# Generated by Django 4.0.1 on 2022-04-09 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_order_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.FloatField(null=True),
        ),
    ]

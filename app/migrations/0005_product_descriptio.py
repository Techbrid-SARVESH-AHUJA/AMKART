# Generated by Django 3.1.4 on 2021-06-12 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_product_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='descriptio',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

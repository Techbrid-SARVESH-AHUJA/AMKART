# Generated by Django 3.1.4 on 2021-06-13 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_auto_20210613_2242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='view_mobile',
            old_name='identity_data',
            new_name='identity_number',
        ),
    ]

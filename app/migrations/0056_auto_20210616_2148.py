# Generated by Django 3.1.4 on 2021-06-16 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0055_auto_20210616_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_us_form',
            name='e_mail',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='contact_us_form',
            name='message',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='contact_us_form',
            name='name',
            field=models.TextField(null=True),
        ),
    ]
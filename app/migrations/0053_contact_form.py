# Generated by Django 3.1.4 on 2021-06-16 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0052_lego_model_model_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('e_mail', models.CharField(max_length=200, null=True)),
                ('message', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]

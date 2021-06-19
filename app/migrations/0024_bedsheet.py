# Generated by Django 3.1.4 on 2021-06-13 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_categorie_mb'),
    ]

    operations = [
        migrations.CreateModel(
            name='bedsheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(upload_to='static')),
                ('price', models.IntegerField(max_length=200, null=True)),
                ('size', models.CharField(max_length=200, null=True)),
                ('material', models.CharField(max_length=200, null=True)),
                ('type', models.CharField(max_length=200, null=True)),
                ('pattern', models.CharField(max_length=200, null=True)),
                ('wash_care', models.CharField(max_length=200, null=True)),
                ('color', models.CharField(max_length=200, null=True)),
                ('style', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]

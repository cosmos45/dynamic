# Generated by Django 3.1 on 2020-08-27 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nav', '0005_pastelpainting'),
    ]

    operations = [
        migrations.CreateModel(
            name='InkPainting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000)),
                ('artist', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]

# Generated by Django 3.1 on 2020-08-28 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nav', '0006_inkpainting'),
    ]

    operations = [
        migrations.AddField(
            model_name='abstractpainting',
            name='integer',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='acrylicpainting',
            name='integer',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inkpainting',
            name='integer',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pastelpainting',
            name='integer',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
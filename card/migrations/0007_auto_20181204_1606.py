# Generated by Django 2.1.1 on 2018-12-04 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0006_auto_20181113_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='description',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='card',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='card',
            name='rare',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 2.1.5 on 2019-03-04 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20190304_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
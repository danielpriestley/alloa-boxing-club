# Generated by Django 2.0.10 on 2019-02-27 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_profile_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fights',
            field=models.IntegerField(default=1),
        ),
    ]

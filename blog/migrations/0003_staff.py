# Generated by Django 2.1.5 on 2019-03-19 09:29

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_remove_coach_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('forename', models.CharField(max_length=50)),
                ('surname', models.CharField(blank=True, default='Boxer', max_length=20)),
                ('age', models.IntegerField(default=16)),
                ('experience', models.IntegerField(default=1)),
                ('bio', models.TextField(default='')),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

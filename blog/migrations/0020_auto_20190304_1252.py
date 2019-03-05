# Generated by Django 2.1.5 on 2019-03-04 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0019_auto_20190303_2140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventTitle', models.CharField(blank=True, default='', max_length=100)),
                ('eventDate', models.CharField(blank=True, default='', max_length=100)),
                ('price', models.CharField(blank=True, default='', max_length=100)),
                ('homeFighter', models.CharField(blank=True, default='', max_length=100)),
                ('homeClub', models.CharField(blank=True, default='', max_length=100)),
                ('awayFighter', models.CharField(blank=True, default='', max_length=100)),
                ('awayClub', models.CharField(blank=True, default='', max_length=100)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='surname',
            field=models.CharField(blank=True, default='Boxer', max_length=20),
        ),
    ]

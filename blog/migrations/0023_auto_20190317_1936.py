# Generated by Django 2.1.5 on 2019-03-17 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_galleryphoto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='galleryphoto',
            old_name='title',
            new_name='credit',
        ),
    ]

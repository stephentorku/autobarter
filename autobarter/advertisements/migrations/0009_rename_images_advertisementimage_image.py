# Generated by Django 3.2.12 on 2022-04-09 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0008_auto_20220409_0928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisementimage',
            old_name='images',
            new_name='image',
        ),
    ]

# Generated by Django 4.0.5 on 2022-09-22 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cat_inf', '0012_injury'),
    ]

    operations = [
        migrations.RenameField(
            model_name='injury',
            old_name='complaint_kind',
            new_name='injury_kind',
        ),
    ]

# Generated by Django 4.0.4 on 2022-08-06 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat_inf', '0002_cat_delete_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='cat_photo'),
        ),
    ]
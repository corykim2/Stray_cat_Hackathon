# Generated by Django 4.0.6 on 2022-08-17 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat_inf', '0004_delete_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

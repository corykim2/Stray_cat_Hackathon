# Generated by Django 4.0.6 on 2022-09-20 23:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat_inf', '0004_alter_complaint_author_alter_complaint_cat_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 9, 20, 23, 48, 43, 185609)),
            preserve_default=False,
        ),
    ]

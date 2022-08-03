# Generated by Django 4.0.6 on 2022-08-03 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat_inf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('info2', models.CharField(max_length=100)),
                ('info3', models.CharField(max_length=100)),
                ('info4', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(decimal_places=13, max_digits=17)),
                ('longitude', models.DecimalField(decimal_places=13, max_digits=17)),
            ],
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]

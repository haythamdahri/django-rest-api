# Generated by Django 2.2.5 on 2019-09-07 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='content',
            field=models.TextField(max_length=5600),
        ),
    ]

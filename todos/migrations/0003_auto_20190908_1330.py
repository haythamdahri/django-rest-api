# Generated by Django 2.2.5 on 2019-09-08 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_auto_20190907_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated At'),
        ),
    ]

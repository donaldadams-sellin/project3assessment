# Generated by Django 3.2.9 on 2022-01-21 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='widget',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
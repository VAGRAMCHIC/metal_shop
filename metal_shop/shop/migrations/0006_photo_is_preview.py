# Generated by Django 2.2.12 on 2022-03-10 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20220310_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='is_preview',
            field=models.BooleanField(default=False),
        ),
    ]
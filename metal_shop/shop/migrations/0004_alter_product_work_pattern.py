# Generated by Django 4.0.4 on 2022-04-15 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_workpattern'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='work_pattern',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.workpattern'),
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-14 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driving', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='chapter',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='driving.chapter'),
        ),
    ]

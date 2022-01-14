# Generated by Django 4.0.1 on 2022-01-14 12:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(validators=[django.core.validators.MaxLengthValidator(2000)])),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(validators=[django.core.validators.MaxLengthValidator(100)])),
                ('picture', models.ImageField(upload_to='')),
                ('answer', models.TextField(validators=[django.core.validators.MaxLengthValidator(100)])),
                ('explanation', models.TextField(validators=[django.core.validators.MaxLengthValidator(2000)])),
                ('chapter', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='driving.chapter')),
            ],
        ),
    ]

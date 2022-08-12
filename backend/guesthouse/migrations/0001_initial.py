# Generated by Django 4.0.7 on 2022-08-03 10:19

import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.EmailField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. email will be used as username. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()])),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stay', models.CharField(max_length=30)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='guesthouse.guest')),
            ],
        ),
    ]
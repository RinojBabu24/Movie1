# Generated by Django 5.0.7 on 2024-07-14 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(help_text='Enter the task', max_length=100)),
                ('date', models.DateField(help_text='Enter the date of the task')),
                ('time', models.TimeField(help_text='Enter the time of the task')),
            ],
        ),
        migrations.DeleteModel(
            name='todo',
        ),
    ]

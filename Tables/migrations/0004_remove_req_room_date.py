# Generated by Django 4.0 on 2023-03-12 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tables', '0003_alter_req_room_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='req_room',
            name='date',
        ),
    ]

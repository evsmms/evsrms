# Generated by Django 3.2.5 on 2022-04-26 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_auto_20220426_1356'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serviceticket',
            old_name='service_ticket',
            new_name='vehicle',
        ),
    ]

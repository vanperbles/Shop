# Generated by Django 2.2.9 on 2020-01-10 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_auto_20200110_1534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='stuff',
            new_name='staff',
        ),
    ]

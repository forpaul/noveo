# Generated by Django 2.2.2 on 2019-08-14 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20190814_1523'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='groups',
            new_name='group',
        ),
    ]

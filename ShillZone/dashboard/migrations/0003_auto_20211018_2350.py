# Generated by Django 3.2.7 on 2021-10-18 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20211018_2334'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adduser',
            options={'verbose_name_plural': 'Add User'},
        ),
        migrations.AlterModelTable(
            name='adduser',
            table='add_user',
        ),
    ]

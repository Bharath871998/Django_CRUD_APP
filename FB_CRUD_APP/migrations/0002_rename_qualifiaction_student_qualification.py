# Generated by Django 4.0.2 on 2022-07-25 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FB_CRUD_APP', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='qualifiaction',
            new_name='qualification',
        ),
    ]

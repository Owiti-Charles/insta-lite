# Generated by Django 2.2.6 on 2019-10-14 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0017_auto_20191014_0700'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='follow',
            new_name='follower',
        ),
    ]

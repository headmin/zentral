# Generated by Django 2.2.3 on 2019-09-29 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('munki', '0005_auto_20190227_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='munkistate',
            name='binaryinfo_last_seen',
        ),
    ]

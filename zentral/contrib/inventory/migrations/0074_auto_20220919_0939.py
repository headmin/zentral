# Generated by Django 3.2.14 on 2022-09-19 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0073_alter_metabusinessunit_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='has_removal_passcode',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='encrypted',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='signed_by',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.PROTECT, to='inventory.certificate'),
        ),
    ]

# Generated by Django 2.2.18 on 2021-05-26 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realms', '0006_realmgroupmapping'),
        ('inventory', '0056_machine_snapshot_program_instances_on_delete_cascade'),
        ('mdm', '0035_auto_20210526_0518'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEnrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('enrollment_secret', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='user_enrollment', to='inventory.EnrollmentSecret')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='UserEnrollmentSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.TextField()),
                ('version', models.TextField()),
                ('imei', models.CharField(max_length=18, null=True)),
                ('meid', models.CharField(max_length=18, null=True)),
                ('language', models.CharField(max_length=64, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('STARTED', 'Started'), ('SCEP_VERIFIED', 'SCEP verified'), ('AUTHENTICATED', 'Authenticated'), ('COMPLETED', 'Completed')], max_length=64)),
                ('managed_apple_id', models.EmailField(max_length=254)),
                ('enrolled_device', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mdm.EnrolledDevice')),
                ('enrollment_secret', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='user_enrollment_session', to='inventory.EnrollmentSecret')),
                ('realm_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='realms.RealmUser')),
                ('scep_request', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='inventory.EnrollmentSecretRequest')),
                ('user_enrollment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mdm.UserEnrollment')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

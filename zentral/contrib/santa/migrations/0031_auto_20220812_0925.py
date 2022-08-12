# Generated by Django 3.2.14 on 2022-08-12 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('santa', '0030_auto_20220812_0615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configuration',
            name='banned_block_message',
        ),
        migrations.RemoveField(
            model_name='configuration',
            name='client_auth_certificate_issuer_cn',
        ),
        migrations.RemoveField(
            model_name='configuration',
            name='enable_bad_signature_protection',
        ),
        migrations.RemoveField(
            model_name='configuration',
            name='enable_page_zero_protection',
        ),
        migrations.RemoveField(
            model_name='configuration',
            name='enable_sysx_cache',
        ),
        migrations.RemoveField(
            model_name='configuration',
            name='event_detail_text',
        ),
        migrations.RemoveField(
            model_name='configuration',
            name='event_detail_url',
        ),
        migrations.RemoveField(
            model_name='configuration',
            name='file_changes_prefix_filters',
        ),
        migrations.RemoveField(
            model_name='configuration',
            name='file_changes_regex',
        ),
        migrations.RemoveField(
            model_name='configuration',
            name='machine_owner_key',
        ),
        migrations.RemoveField(
            model_name='configuration',
            name='machine_owner_plist',
        ),
        migrations.RemoveField(
            model_name='configuration',
            name='mode_notification_lockdown',
        ),
        migrations.RemoveField(
            model_name='configuration',
            name='mode_notification_monitor',
        ),
        migrations.RemoveField(
            model_name='configuration',
            name='more_info_url',
        ),
        migrations.RemoveField(
            model_name='configuration',
            name='unknown_block_message',
        ),
        migrations.AlterField(
            model_name='configuration',
            name='client_certificate_auth',
            field=models.BooleanField(
                default=False,
                help_text='If set, a client certificate will be required for sync authentication. '
                          'Santa will automatically look for a matching certificate and its private key '
                          'in the System keychain, if the TLS server advertises the accepted CA certificates. '
                          'If the CA certificates are not sent to the client, use the Client Auth Certificate '
                          'Issuer CN setting in the configuration profile.',
                verbose_name='Client certificate authentication'
            ),
        ),
    ]

# Generated by Django 2.2.20 on 2021-08-31 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0154_set_default_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='instance',
            name='errors',
            field=models.TextField(blank=True, default='', editable=False, help_text='Any error details from the last health check.'),
        ),
        migrations.AddField(
            model_name='instance',
            name='last_health_check',
            field=models.DateTimeField(
                editable=False, help_text='Last time a health check was ran on this instance to refresh cpu, memory, and capacity.', null=True
            ),
        ),
    ]
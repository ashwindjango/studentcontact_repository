# Generated by Django 3.0 on 2020-04-15 18:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('studentcontactapp', '0002_auto_20200415_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdata',
            name='gender',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
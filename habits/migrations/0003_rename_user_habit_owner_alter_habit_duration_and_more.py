# Generated by Django 4.2.5 on 2023-09-05 12:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habit',
            old_name='user',
            new_name='owner',
        ),
        migrations.AlterField(
            model_name='habit',
            name='duration',
            field=models.PositiveSmallIntegerField(default=datetime.timedelta(seconds=120), verbose_name='время на выполнение'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='reward',
            field=models.CharField(blank=True, default=None, max_length=150, null=True, verbose_name='вознаграждение'),
        ),
    ]

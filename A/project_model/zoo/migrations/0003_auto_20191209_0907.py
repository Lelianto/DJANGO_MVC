# Generated by Django 3.0 on 2019-12-09 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0002_auto_20191209_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pengunjung',
            name='hari_berkunjung',
            field=models.DateTimeField(verbose_name='hari berkunjung'),
        ),
    ]

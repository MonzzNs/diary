# Generated by Django 3.0.6 on 2020-06-01 07:49

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200528_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from=models.CharField(blank=True, max_length=250, verbose_name='Title')),
        ),
    ]

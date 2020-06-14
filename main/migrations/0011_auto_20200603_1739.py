# Generated by Django 3.0.6 on 2020-06-03 10:39

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200603_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=True, populate_from='title', unique=True),
        ),
    ]
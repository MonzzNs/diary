# Generated by Django 3.0.3 on 2020-05-25 04:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200519_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
    ]

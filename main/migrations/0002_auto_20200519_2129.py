# Generated by Django 3.0.3 on 2020-05-19 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='title',
            field=models.CharField(blank=True, max_length=250, verbose_name='Title'),
        ),
    ]
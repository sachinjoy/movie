# Generated by Django 4.0.5 on 2022-08-26 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default=1, upload_to='', verbose_name='photos'),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.1.5 on 2020-05-06 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200506_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='text-product'),
            preserve_default=False,
        ),
    ]
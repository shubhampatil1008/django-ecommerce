# Generated by Django 2.1.5 on 2020-05-29 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200529_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(default=123, max_length=50),
            preserve_default=False,
        ),
    ]

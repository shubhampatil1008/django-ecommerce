# Generated by Django 2.1.5 on 2020-05-21 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0040_bilingaddress_default_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promo_code', models.CharField(max_length=20)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]

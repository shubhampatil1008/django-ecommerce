# Generated by Django 2.1.5 on 2020-05-10 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_auto_20200510_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bilingaddress',
            name='address_type',
            field=models.CharField(blank=True, choices=[('Home', 'Home'), ('Office', 'Office'), ('Other', 'Other')], max_length=10, null=True),
        ),
    ]

# Generated by Django 2.1.5 on 2020-05-10 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_auto_20200510_0108'),
    ]

    operations = [
        migrations.AddField(
            model_name='bilingaddress',
            name='address_type',
            field=models.CharField(blank=True, choices=[('H', 'Home'), ('OF', 'Office'), ('OT', 'Other')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='label_name',
            field=models.CharField(blank=True, choices=[('N', 'NEW'), ('S', 'SALE'), ('D', 'DISCOUNT'), ('O', 'OFFER')], max_length=1, null=True),
        ),
    ]
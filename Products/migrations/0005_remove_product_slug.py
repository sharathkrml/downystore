# Generated by Django 3.2.7 on 2021-09-04 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_alter_product_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
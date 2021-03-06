# Generated by Django 3.2.6 on 2021-09-03 09:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0004_card_exp_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Orders', '0002_remove_cart_cart_total_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_status', models.CharField(max_length=30)),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('total_price', models.IntegerField()),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.address')),
                ('cart_ids', models.ManyToManyField(to='Orders.Cart')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

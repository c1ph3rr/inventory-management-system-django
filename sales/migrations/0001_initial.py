# Generated by Django 4.0.5 on 2022-07-04 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesModel',
            fields=[
                ('order_no', models.IntegerField(primary_key=True, serialize=False)),
                ('customer', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventorymodel')),
            ],
        ),
    ]
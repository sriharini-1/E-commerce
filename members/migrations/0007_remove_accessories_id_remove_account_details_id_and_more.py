# Generated by Django 5.0.2 on 2024-03-01 18:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_accessories_order_items_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accessories',
            name='id',
        ),
        migrations.RemoveField(
            model_name='account_details',
            name='id',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='id',
        ),
        migrations.RemoveField(
            model_name='category',
            name='id',
        ),
        migrations.RemoveField(
            model_name='order_items',
            name='id',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='id',
        ),
        migrations.RemoveField(
            model_name='products',
            name='id',
        ),
        migrations.AddField(
            model_name='accessories',
            name='accessoryID',
            field=models.CharField(default='1', max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='accessories',
            name='brandID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='members.brand'),
        ),
        migrations.AddField(
            model_name='accessories',
            name='categoryID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='members.category'),
        ),
        migrations.AddField(
            model_name='account_details',
            name='userID',
            field=models.CharField(default='1', max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='brand',
            name='brandID',
            field=models.CharField(default='1', max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='category',
            name='categoryID',
            field=models.CharField(default='1', max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='order_items',
            name='itemID',
            field=models.CharField(default='1', max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='order_items',
            name='orderID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='members.orders'),
        ),
        migrations.AddField(
            model_name='order_items',
            name='productID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='members.products'),
        ),
        migrations.AddField(
            model_name='orders',
            name='orderID',
            field=models.CharField(default='1', max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='orders',
            name='userID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='members.account_details'),
        ),
        migrations.AddField(
            model_name='products',
            name='brandID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='members.brand'),
        ),
        migrations.AddField(
            model_name='products',
            name='categoryID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='members.category'),
        ),
        migrations.AddField(
            model_name='products',
            name='productID',
            field=models.CharField(default='1', max_length=20, primary_key=True, serialize=False),
        ),
    ]

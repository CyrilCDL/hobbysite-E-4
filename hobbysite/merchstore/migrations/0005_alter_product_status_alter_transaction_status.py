# Generated by Django 5.0.2 on 2024-05-08 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchstore', '0004_product_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Available'), ('ON SALE', 'On Sale'), ('OUT OF STOCK', 'Out of Stock')], default='AVAILABLE', max_length=50),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('ON CART', 'On Cart'), ('TO PAY', 'To Pay'), ('TO SHIP', 'To Ship'), ('TO RECEIVE', 'To Receive'), ('DELIVERED', 'Delivered')], default='ON CART', max_length=20),
        ),
    ]
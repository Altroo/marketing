# Generated by Django 4.0.2 on 2022-03-01 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0007_alter_seller_processed_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='collections',
            field=models.ManyToManyField(related_name='product_collections', to='seller.Collection', verbose_name='Collections'),
        ),
    ]
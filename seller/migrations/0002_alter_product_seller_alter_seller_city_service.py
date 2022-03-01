# Generated by Django 4.0.2 on 2022-02-28 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_seller', to='seller.seller', verbose_name='Vendeur'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller_city', to='seller.cities', verbose_name='Ville'),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_title', models.CharField(max_length=150, verbose_name='Titre de service')),
                ('service_link', models.URLField(blank=True, default=None, null=True, verbose_name='Lien de service')),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('category', models.ManyToManyField(related_name='service_categories', to='seller.Categories', verbose_name='Categories')),
                ('cible', models.ManyToManyField(blank=True, null=True, related_name='service_cible', to='seller.Cible', verbose_name='Cible')),
                ('seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_seller', to='seller.seller', verbose_name='Vendeur')),
                ('service_city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_city', to='seller.cities', verbose_name='Ville')),
                ('sous_category', models.ManyToManyField(blank=True, null=True, related_name='service_sous_categories', to='seller.SousCategories', verbose_name='Sous-categorie')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
                'ordering': ('created_date',),
            },
        ),
    ]
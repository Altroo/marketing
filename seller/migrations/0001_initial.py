# Generated by Django 4.0.2 on 2022-02-28 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=255, unique=True, verbose_name='Categorie')),
            ],
            options={
                'verbose_name': 'Categorie',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Cible',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_cible', models.CharField(max_length=255, unique=True, verbose_name='Cible')),
            ],
            options={
                'verbose_name': 'Cible',
                'verbose_name_plural': 'Cible',
            },
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_en', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='City EN')),
                ('city_fr', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='City FR')),
                ('city_ar', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='City AR')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_name', models.CharField(max_length=150, verbose_name='Nom de collection')),
                ('h1', models.CharField(max_length=150, verbose_name='H1')),
                ('collection_link', models.URLField(blank=True, default=None, null=True, verbose_name='URL de la collection')),
                ('meta_description', models.TextField(verbose_name='Meta-description')),
                ('paragraphe', models.TextField(verbose_name='Paragraphe')),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
            ],
            options={
                'verbose_name': 'Collection',
                'verbose_name_plural': 'Collections',
                'ordering': ('created_date',),
            },
        ),
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_color', models.CharField(max_length=255, unique=True, verbose_name='Couleur')),
            ],
            options={
                'verbose_name': 'Couleur',
                'verbose_name_plural': 'Couleurs',
            },
        ),
        migrations.CreateModel(
            name='SousCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_sous_category', models.CharField(max_length=255, unique=True, verbose_name='Sous-Categorie')),
            ],
            options={
                'verbose_name': 'Sous-categorie',
                'verbose_name_plural': 'Sous-categories',
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_name', models.CharField(max_length=150, verbose_name='Nom du vendeur')),
                ('seller_link', models.URLField(blank=True, default=None, null=True, verbose_name='Coordonnées du vendeur')),
                ('number_of_products', models.IntegerField(verbose_name='Nombre de produits')),
                ('seller_status', models.CharField(choices=[('NC', 'Non contacté'), ('NI', 'Non inscrit'), ('PR', 'Pas de réponse'), ('GR', 'Gratuit'), ('PA', 'Payant')], default='NC', max_length=2, verbose_name='Statut du vendeur')),
                ('seller_type', models.CharField(choices=[('V', 'Vendeur'), ('C', 'Créateur')], default='V', max_length=1, verbose_name='Type de vendeur')),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='seller_city', to='seller.cities', verbose_name='Ville')),
            ],
            options={
                'verbose_name': 'Vendeur',
                'verbose_name_plural': 'Vendeurs',
                'ordering': ('created_date',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=150, verbose_name='Titre de produit')),
                ('product_link', models.URLField(blank=True, default=None, null=True, verbose_name='Lien de produit')),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
                ('category', models.ManyToManyField(related_name='product_categories', to='seller.Categories', verbose_name='Categories')),
                ('cible', models.ManyToManyField(blank=True, null=True, related_name='product_cible', to='seller.Cible', verbose_name='Cible')),
                ('color', models.ForeignKey(max_length=2, on_delete=django.db.models.deletion.CASCADE, related_name='product_color', to='seller.colors', verbose_name='Couleur produit')),
                ('seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_seller', to='seller.seller', verbose_name='Vendeur')),
                ('sous_category', models.ManyToManyField(blank=True, null=True, related_name='product_sous_categories', to='seller.SousCategories', verbose_name='Sous-categorie')),
            ],
            options={
                'verbose_name': 'Produit',
                'verbose_name_plural': 'Produits',
                'ordering': ('created_date',),
            },
        ),
    ]

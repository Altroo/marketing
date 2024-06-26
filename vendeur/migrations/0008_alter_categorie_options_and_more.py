# Generated by Django 4.0.3 on 2022-03-04 10:36

import django.contrib.postgres.fields.citext
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendeur', '0007_alter_groupedeproduit_titre_groupe_de_produit_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorie',
            options={'ordering': ('pk',), 'verbose_name': ' Catégorie', 'verbose_name_plural': ' Catégories'},
        ),
        migrations.AlterModelOptions(
            name='groupedeproduit',
            options={'ordering': ('pk',), 'verbose_name': ' Produit', 'verbose_name_plural': ' Produits'},
        ),
        migrations.AlterModelOptions(
            name='produit',
            options={'ordering': ('pk',), 'verbose_name': ' Tag', 'verbose_name_plural': ' Tags'},
        ),
        migrations.AlterModelOptions(
            name='vendeur',
            options={'ordering': ('pk',), 'verbose_name': '  Vendeur', 'verbose_name_plural': '  Vendeurs'},
        ),
        migrations.AlterField(
            model_name='groupedeproduit',
            name='titre_groupe_de_produit',
            field=django.contrib.postgres.fields.citext.CICharField(max_length=255, unique=True, verbose_name='Titre de produit'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='titre_produit',
            field=django.contrib.postgres.fields.citext.CICharField(max_length=255, unique=True, verbose_name='Titre Tag'),
        ),
        migrations.AlterField(
            model_name='vendeurcategorie',
            name='groupe_de_produit',
            field=models.ManyToManyField(related_name='vendeurcategorie_groupe_de_produit', to='vendeur.groupedeproduit', verbose_name='Produit'),
        ),
        migrations.AlterField(
            model_name='vendeurcategorie',
            name='produit',
            field=models.ManyToManyField(related_name='vendeurcategorie_produit', to='vendeur.produit', verbose_name='Tag'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-04 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendeur', '0003_categorie_referencer_categorie_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='lien_categorie',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='groupedeproduit',
            name='lien_groupe_de_produit',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='lien_produit',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='style',
            name='lien_style',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='vendeurcategorie',
            name='lien_vendeurcategorie',
            field=models.URLField(blank=True, default=None, null=True, verbose_name='URL'),
        ),
    ]

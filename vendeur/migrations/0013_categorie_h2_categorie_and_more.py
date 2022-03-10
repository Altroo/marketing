# Generated by Django 4.0.3 on 2022-03-10 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendeur', '0012_categorie_page_title_groupedeproduit_page_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='h2_categorie',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='H2'),
        ),
        migrations.AddField(
            model_name='groupedeproduit',
            name='h2_groupe_de_produit',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='H2'),
        ),
        migrations.AddField(
            model_name='produit',
            name='h2_produit',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='H2'),
        ),
        migrations.AddField(
            model_name='style',
            name='h2_style',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='H2'),
        ),
    ]
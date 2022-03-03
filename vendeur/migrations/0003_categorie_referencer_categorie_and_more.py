# Generated by Django 4.0.3 on 2022-03-03 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendeur', '0002_alter_vendeurcategorie_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='referencer_categorie',
            field=models.BooleanField(default=False, verbose_name='Référencé'),
        ),
        migrations.AddField(
            model_name='groupedeproduit',
            name='referencer_groupe_de_produit',
            field=models.BooleanField(default=False, verbose_name='Référencé'),
        ),
        migrations.AddField(
            model_name='produit',
            name='referencer_produit',
            field=models.BooleanField(default=False, verbose_name='Référencé'),
        ),
        migrations.AddField(
            model_name='style',
            name='referencer_style',
            field=models.BooleanField(default=False, verbose_name='Référencé'),
        ),
    ]

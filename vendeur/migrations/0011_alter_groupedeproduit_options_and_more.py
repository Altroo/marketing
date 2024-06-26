# Generated by Django 4.0.3 on 2022-03-07 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendeur', '0010_alter_vendeurcategorie_lien_vendeurcategorie'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groupedeproduit',
            options={'ordering': ('pk',), 'verbose_name': ' Collection', 'verbose_name_plural': ' Collections'},
        ),
        migrations.AlterField(
            model_name='vendeurcategorie',
            name='groupe_de_produit',
            field=models.ManyToManyField(related_name='vendeurcategorie_groupe_de_produit', to='vendeur.groupedeproduit', verbose_name='Collection'),
        ),
        migrations.AlterField(
            model_name='vendeurcategorie',
            name='produit',
            field=models.ManyToManyField(blank=True, related_name='vendeurcategorie_produit', to='vendeur.produit', verbose_name='Tag'),
        ),
    ]

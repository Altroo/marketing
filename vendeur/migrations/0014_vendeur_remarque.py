# Generated by Django 4.0.3 on 2022-03-16 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendeur', '0013_categorie_h2_categorie_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendeur',
            name='remarque',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Remarque'),
        ),
    ]

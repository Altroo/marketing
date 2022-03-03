from django.db import models
from django.db.models import Model


class Cible(Model):
    name_cible = models.CharField(max_length=255, verbose_name='Cible', unique=True)

    def __str__(self):
        return '{}'.format(self.name_cible)

    class Meta:
        verbose_name = 'Cible'
        verbose_name_plural = 'Cible'


class Vendeur(Model):
    nom_vendeur = models.CharField(verbose_name='Nom vendeur', max_length=150, blank=False, null=False)
    SELLER_TYPE_CHOICES = (
        ('V', 'Vendeur'),
        ('C', 'Créateur'),
    )
    type_vendeur = models.CharField(verbose_name='Type vendeur', max_length=2,
                                    choices=SELLER_TYPE_CHOICES, default='V')
    lien_vendeur = models.URLField(verbose_name='Lien du vendeur', blank=True, null=True, default=None)
    pipass = models.BooleanField(verbose_name='Pipass', default=False)
    contacter = models.BooleanField(verbose_name='Contacté', default=False)

    # Dates
    created_date = models.DateTimeField(verbose_name='Created date', editable=False, auto_now_add=True, db_index=True)
    updated_date = models.DateTimeField(verbose_name='Updated date', editable=False, auto_now=True)

    def __str__(self):
        return '{}'.format(self.nom_vendeur)

    class Meta:
        verbose_name = 'Vendeur'
        verbose_name_plural = 'Vendeurs'
        ordering = ('pk',)


class Categorie(Model):
    titre_categorie = models.CharField(max_length=255, verbose_name='Titre catégorie', unique=True)
    lien_categorie = models.URLField(verbose_name='Lien catégorie', blank=True, null=True, default=None)
    meta_description_categorie = models.TextField(verbose_name='Meta-déscription', blank=True, null=True)
    h1_categorie = models.CharField(verbose_name='H1', max_length=150, blank=True, null=True)
    paragraphe_categorie = models.TextField(verbose_name='Paragraphe', blank=True, null=True)
    referencer_categorie = models.BooleanField(verbose_name='Référencé', default=False)

    def __str__(self):
        return '{}'.format(self.titre_categorie)

    class Meta:
        verbose_name = 'Catégorie'
        verbose_name_plural = 'Catégories'
        ordering = ('pk',)


class GroupeDeProduit(Model):
    titre_groupe_de_produit = models.CharField(max_length=255, verbose_name='Titre groupe de produit', unique=True)
    lien_groupe_de_produit = models.URLField(verbose_name='Lien groupe de produit', blank=True, null=True, default=None)
    meta_description_groupe_de_produit = models.TextField(verbose_name='Meta-déscription', blank=True, null=True)
    h1_groupe_de_produit = models.CharField(verbose_name='H1', max_length=150, blank=True, null=True)
    paragraphe_groupe_de_produit = models.TextField(verbose_name='Paragraphe', blank=True, null=True)
    referencer_groupe_de_produit = models.BooleanField(verbose_name='Référencé', default=False)

    def __str__(self):
        return '{}'.format(self.titre_groupe_de_produit)

    class Meta:
        verbose_name = 'Groupe de produit'
        verbose_name_plural = 'Groupe de produits'
        ordering = ('pk',)


class Produit(Model):
    titre_produit = models.CharField(max_length=255, verbose_name='Titre produit', unique=True)
    lien_produit = models.URLField(verbose_name='Lien produit', blank=True, null=True, default=None)
    meta_description_produit = models.TextField(verbose_name='Meta-déscription', blank=True, null=True)
    h1_produit = models.CharField(verbose_name='H1', max_length=150, blank=True, null=True)
    paragraphe_produit = models.TextField(verbose_name='Paragraphe', blank=True, null=True)
    referencer_produit = models.BooleanField(verbose_name='Référencé', default=False)

    def __str__(self):
        return '{}'.format(self.titre_produit)

    class Meta:
        verbose_name = 'Produit'
        verbose_name_plural = 'Produits'
        ordering = ('pk',)


class Style(Model):
    titre_style = models.CharField(max_length=255, verbose_name='Titre style', unique=True)
    lien_style = models.URLField(verbose_name='Lien style', blank=True, null=True, default=None)
    meta_description_style = models.TextField(verbose_name='Meta-déscription', blank=True, null=True)
    h1_style = models.CharField(verbose_name='H1', max_length=150, blank=True, null=True)
    paragraphe_style = models.TextField(verbose_name='Paragraphe', blank=True, null=True)
    referencer_style = models.BooleanField(verbose_name='Référencé', default=False)

    def __str__(self):
        return '{}'.format(self.titre_style)

    class Meta:
        verbose_name = 'Style'
        verbose_name_plural = 'Styles'
        ordering = ('pk',)


class VendeurCategorie(Model):
    vendeur = models.ForeignKey(Vendeur, verbose_name='Vendeur', blank=True, null=True, on_delete=models.CASCADE,
                                related_name='vendeurcategorie_vendeur')
    categorie = models.ManyToManyField(Categorie, verbose_name='Categories', related_name='vendeurcategorie_categorie')
    groupe_de_produit = models.ManyToManyField(GroupeDeProduit, verbose_name='Groupe de produit', blank=True,
                                               related_name='vendeurcategorie_groupe_de_produit')
    produit = models.ManyToManyField(Produit, verbose_name='Produit', blank=True,
                                     related_name='vendeurcategorie_produit')
    style = models.ManyToManyField(Style, verbose_name='Style', blank=True,
                                   related_name='vendeurcategorie_style')
    cible = models.ManyToManyField(Cible, verbose_name='Cible', blank=True,
                                   related_name='vendeurcategorie_cible')
    lien_vendeurcategorie = models.URLField(verbose_name='Lien', blank=True, null=True, default=None)

    def __str__(self):
        return '{}'.format(self.vendeur.nom_vendeur)

    class Meta:
        verbose_name = 'Produit de vendeur'
        verbose_name_plural = 'Produits de vendeur'
        ordering = ('pk',)
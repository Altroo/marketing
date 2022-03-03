from django.db import models
from django.db.models import Model


class MarketingChoices:
    SELLER_STATUS_CHOICES = (
        ('NC', 'Non contacté'),
        ('NI', 'Non inscrit'),
        ('PR', 'Pas de réponse'),
        ('GR', 'Gratuit'),
        ('PA', 'Payant'),
    )

    SELLER_TYPE_CHOICES = (
        ('V', 'Vendeur'),
        ('C', 'Créateur'),
    )


class Cities(Model):
    city_en = models.CharField(max_length=255, verbose_name='City EN', blank=True, null=True, default=None)
    city_fr = models.CharField(max_length=255, verbose_name='City FR', blank=True, null=True, default=None)
    city_ar = models.CharField(max_length=255, verbose_name='City AR', blank=True, null=True, default=None)

    def __str__(self):
        return '{}'.format(self.city_fr)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class Seller(Model):
    seller_name = models.CharField(verbose_name='Nom du vendeur', max_length=150, blank=False, null=False)
    seller_link = models.URLField(verbose_name='Coordonnées du vendeur', blank=True, null=True, default=None)
    city = models.ForeignKey(Cities, verbose_name='Ville', blank=True, null=True, on_delete=models.CASCADE,
                             related_name='seller_city')
    number_of_products = models.IntegerField(verbose_name='Nombre de produits', blank=False, null=False)
    seller_status = models.CharField(verbose_name='Status du vendeur', max_length=2,
                                     choices=MarketingChoices.SELLER_STATUS_CHOICES, default='NC')
    seller_type = models.CharField(verbose_name='Type de vendeur', max_length=1,
                                   choices=MarketingChoices.SELLER_TYPE_CHOICES, default='V')
    processed_status = models.BooleanField(verbose_name='Traiter', default=False)
    pipass = models.BooleanField(verbose_name='Pipass', default=False)
    # Dates
    created_date = models.DateTimeField(verbose_name='Created date', editable=False, auto_now_add=True, db_index=True)
    updated_date = models.DateTimeField(verbose_name='Updated date', editable=False, auto_now=True)

    def __str__(self):
        return '{}'.format(self.seller_name)

    class Meta:
        verbose_name = 'Vendeur'
        verbose_name_plural = 'Vendeurs'
        ordering = ('seller_name',)


class Categories(Model):
    name_category = models.CharField(max_length=255, verbose_name='Categorie', unique=True)

    def __str__(self):
        return '{}'.format(self.name_category)

    class Meta:
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'


class SousCategories(Model):
    name_sous_category = models.CharField(max_length=255, verbose_name='Sous-Categorie', unique=True)

    def __str__(self):
        return '{}'.format(self.name_sous_category)

    class Meta:
        verbose_name = 'Sous-categorie'
        verbose_name_plural = 'Sous-categories'


class Cible(Model):
    name_cible = models.CharField(max_length=255, verbose_name='Cible', unique=True)

    def __str__(self):
        return '{}'.format(self.name_cible)

    class Meta:
        verbose_name = 'Cible'
        verbose_name_plural = 'Cible'


class Colors(Model):
    name_color = models.CharField(max_length=255, verbose_name='Couleur', unique=True)

    def __str__(self):
        return '{}'.format(self.name_color)

    class Meta:
        verbose_name = 'Couleur'
        verbose_name_plural = 'Couleurs'


class OfferType(Model):
    name_offer = models.CharField(max_length=255, verbose_name='Offre type', unique=True)

    def __str__(self):
        return '{}'.format(self.name_offer)

    class Meta:
        verbose_name = 'Offer type'
        verbose_name_plural = 'Offer types'


class Collection(Model):
    collection_name = models.CharField(verbose_name='Nom de collection', max_length=150, blank=False, null=False)
    h1 = models.CharField(verbose_name='H1', max_length=150, blank=False, null=False)
    collection_link = models.URLField(verbose_name='URL de la collection', blank=True, null=True, default=None)
    meta_description = models.TextField(verbose_name='Meta-description', blank=False, null=False)
    paragraphe = models.TextField(verbose_name='Paragraphe', blank=False, null=False)

    # Dates
    created_date = models.DateTimeField(verbose_name='Created date', editable=False, auto_now_add=True, db_index=True)
    updated_date = models.DateTimeField(verbose_name='Updated date', editable=False, auto_now=True)

    def __str__(self):
        return '{}'.format(self.collection_name)

    class Meta:
        verbose_name = 'Collection'
        verbose_name_plural = 'Collections'
        ordering = ('created_date',)


class Product(Model):
    seller = models.ForeignKey(Seller, verbose_name='Vendeur', blank=True, null=True, on_delete=models.CASCADE,
                               related_name='product_seller')
    product_title = models.CharField(verbose_name='Titre du produit', max_length=150, blank=False, null=False)
    category = models.ManyToManyField(Categories, verbose_name='Categories', related_name='product_categories')
    sous_category = models.ManyToManyField(SousCategories, verbose_name='Sous-categorie', blank=True,
                                           related_name='product_sous_categories')
    cible = models.ManyToManyField(Cible, verbose_name='Cible', blank=True, related_name='product_cible')
    product_link = models.URLField(verbose_name='Lien de produit', blank=True, null=True, default=None)
    price = models.FloatField(verbose_name='Prix', default=0.0, blank=True, null=True)
    offer_type = models.ManyToManyField(OfferType, verbose_name="Type d'offre", related_name='product_offer_type')
    color = models.ManyToManyField(Colors, verbose_name='Couleur produit', max_length=2,
                                   related_name='product_color', blank=True)
    collections = models.ManyToManyField(Collection, verbose_name='Collections',
                                         related_name='product_collections', blank=True)
    # Dates
    created_date = models.DateTimeField(verbose_name='Created date', editable=False, auto_now_add=True, db_index=True)
    updated_date = models.DateTimeField(verbose_name='Updated date', editable=False, auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.seller.seller_name, self.product_title)

    class Meta:
        verbose_name = 'Produit'
        verbose_name_plural = 'Produits'
        ordering = ('created_date',)

# class Service(Model):
#     seller = models.ForeignKey(Seller, verbose_name='Vendeur', blank=True, null=True, on_delete=models.CASCADE,
#                                related_name='service_seller')
#     service_title = models.CharField(verbose_name='Titre de service', max_length=150, blank=False, null=False)
#     category = models.ManyToManyField(Categories, verbose_name='Categories', related_name='service_categories')
#     sous_category = models.ManyToManyField(SousCategories, verbose_name='Sous-categorie', blank=True,
#                                            related_name='service_sous_categories')
#     cible = models.ManyToManyField(Cible, verbose_name='Cible', blank=True, related_name='service_cible')
#     service_link = models.URLField(verbose_name='Lien de service', blank=True, null=True, default=None)
#     service_city = models.ForeignKey(Cities, verbose_name='Ville', blank=True, null=True, on_delete=models.CASCADE,
#                                      related_name='service_city')
#
#     # Dates
#     created_date = models.DateTimeField(verbose_name='Created date', editable=False, auto_now_add=True, db_index=True)
#     updated_date = models.DateTimeField(verbose_name='Updated date', editable=False, auto_now=True)
#
#     def __str__(self):
#         return '{} - {} - {}'.format(self.service_title, self.service_link, self.service_city)
#
#     class Meta:
#         verbose_name = 'Service'
#         verbose_name_plural = 'Services'
#         ordering = ('created_date',)

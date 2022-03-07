from django.urls import reverse
from vendeur.models import Produit, GroupeDeProduit, Categorie, Style, Cible
from nested_admin.nested import NestedModelAdmin, NestedStackedInline
from django.contrib import admin
from .models import Vendeur, VendeurCategorie
from django.utils.html import format_html
from more_admin_filters import MultiSelectDropdownFilter


class VendeurCategoriesInline(NestedStackedInline):
    model = VendeurCategorie
    extra = 1
    filter_horizontal = ('categorie', 'groupe_de_produit', 'produit', 'style', 'cible')
    autocomplete_fields = ['categorie', 'groupe_de_produit', 'produit', 'style', 'cible']


class VendeurAdmin(NestedModelAdmin):
    list_display = ('nom_vendeur', 'get_categories_with_link', 'contacter', 'pipass')
    list_editable = ('contacter', 'pipass')
    list_display_links = ('nom_vendeur',)
    search_fields = ('nom_vendeur', 'lien_vendeur', 'vendeurcategorie_vendeur__categorie__titre_categorie')
    ordering = ('-pk',)
    date_hierarchy = 'created_date'
    list_filter = [
        ('vendeurcategorie_vendeur__categorie__titre_categorie', MultiSelectDropdownFilter),
        'type_vendeur', 'pipass', 'contacter'
    ]

    inlines = [
        VendeurCategoriesInline
    ]

    def get_categories_with_link(self, obj):
        categories = set(VendeurCategorie.objects.filter(vendeur=obj.pk).values_list('categorie__pk',
                                                                                     'categorie__titre_categorie'))
        html = '<a href="{reverse}{id}/change/">{name}</a>'
        return format_html(',\n'.join(html.format(reverse=reverse('admin:vendeur_categorie_changelist'),
                                                  id=i, name=v) for i, v in categories))

    get_categories_with_link.short_description = 'Catégorie'
    get_categories_with_link.allow_tags = True


class CategorieAdmin(admin.ModelAdmin):
    list_display = ('titre_categorie', 'get_nbr_groupe_de_produit', 'referencer_categorie', 'utilisateur')
    list_display_links = ('titre_categorie',)
    list_editable = ('referencer_categorie', 'utilisateur')
    list_filter = ('referencer_categorie', 'utilisateur')
    ordering = ('-pk',)
    search_fields = ('titre_categorie',)

    def get_nbr_groupe_de_produit(self, obj):
        vendeur_categories = VendeurCategorie.objects.filter(categorie=obj.pk)
        params = ''
        param_set = set()
        for vendeur_categorie in vendeur_categories:
            try:
                titre_groupe_de_produit = vendeur_categorie.groupe_de_produit.all() \
                    .values_list('titre_groupe_de_produit', flat=True)[0]
                param_set.add(titre_groupe_de_produit)
            except IndexError:
                continue
        for param in param_set:
            params += param + ','
        nbr_group_de_produit = len(param_set)
        if nbr_group_de_produit != 0:
            html = '<a href="{reverse}?titre_groupe_de_produit__in={params}">{nbr}</a>'
            html_ = format_html(html.format(reverse=reverse('admin:vendeur_groupedeproduit_changelist'),
                                            nbr=nbr_group_de_produit, params=params[:-1]))
            return html_
        return 0

    get_nbr_groupe_de_produit.short_description = 'Nbr Collections'
    get_nbr_groupe_de_produit.allow_tags = True

    def get_fields(self, request, obj=None):
        fields = super(CategorieAdmin, self).get_fields(request, obj)
        try:
            groups_list = list(request.user.groups.values_list('name', flat=True))
            if 'Marketing Team' in groups_list:
                fields = ('titre_categorie',)
            else:
                fields = ['titre_categorie', 'lien_categorie',
                          'meta_description_categorie',
                          'h1_categorie',
                          'paragraphe_categorie', 'referencer_categorie']
        except IndexError:
            pass
        return fields

    # def get_users(self, obj):
    #     return User.objects.filter(is_superuser=False)


class ProduitAdmin(admin.ModelAdmin):
    list_display = ('titre_produit', 'get_nbr_vendeurs', 'referencer_produit', 'utilisateur')
    list_display_links = ('titre_produit',)
    list_editable = ('referencer_produit', 'utilisateur')
    list_filter = ('referencer_produit', 'utilisateur')
    ordering = ('-pk',)
    search_fields = ('titre_produit',)

    def get_nbr_vendeurs(self, obj):
        vendeur_categorie = VendeurCategorie.objects.filter(produit=obj.pk)
        params = ''
        param_set = set()
        for vendeur in vendeur_categorie:
            param_set.add(str(vendeur.vendeur.pk))
        for param in param_set:
            params += param + ','
        nbr_vendeur = len(param_set)
        if nbr_vendeur != 0:
            html = '<a href="{reverse}?id__in={params}">{nbr}</a>'
            html_ = format_html(html.format(reverse=reverse('admin:vendeur_vendeur_changelist'),
                                            nbr=nbr_vendeur, params=params[:-1]))
            return html_
        return 0

    get_nbr_vendeurs.short_description = 'Nbr de Vendeurs'
    get_nbr_vendeurs.allow_tags = True

    def get_fields(self, request, obj=None):
        fields = super(ProduitAdmin, self).get_fields(request, obj)
        try:
            groups_list = list(request.user.groups.values_list('name', flat=True))
            if 'Marketing Team' in groups_list:
                fields = ('titre_produit',)
            else:
                fields = ['titre_produit', 'lien_produit',
                          'meta_description_produit',
                          'h1_produit',
                          'paragraphe_produit', 'referencer_produit']
        except IndexError:
            pass
        return fields


class GroupeDeProduitAdmin(admin.ModelAdmin):
    list_display = (
        'titre_groupe_de_produit', 'get_nbr_vendeurs', 'get_nbr_produit', 'referencer_groupe_de_produit', 'utilisateur')
    list_display_links = ('titre_groupe_de_produit',)
    list_editable = ('referencer_groupe_de_produit', 'utilisateur')
    list_filter = ('referencer_groupe_de_produit', 'utilisateur')
    ordering = ('-pk',)
    search_fields = ('titre_groupe_de_produit',)

    def get_nbr_produit(self, obj):
        vendeur_categorie = VendeurCategorie.objects.filter(groupe_de_produit=obj.pk)
        params = ''
        param_set = set()
        for vendeur in vendeur_categorie:
            try:
                titre_produit = vendeur.produit.all().values_list('pk', flat=True)[0]
                param_set.add(str(titre_produit))
            except IndexError:
                continue
        for param in param_set:
            params += param + ','
        nbr_vendeur = len(param_set)
        if nbr_vendeur != 0:
            html = '<a href="{reverse}?id__in={params}">{nbr}</a>'
            html_ = format_html(html.format(reverse=reverse('admin:vendeur_produit_changelist'),
                                            nbr=nbr_vendeur, params=params[:-1]))
            return html_
        return 0

    get_nbr_produit.short_description = 'Nbr de Tags'
    get_nbr_produit.allow_tags = True

    def get_nbr_vendeurs(self, obj):
        vendeur_categorie = VendeurCategorie.objects.filter(groupe_de_produit=obj.pk)
        params = ''
        param_set = set()
        for vendeur in vendeur_categorie:
            param_set.add(str(vendeur.vendeur.pk))
        for param in param_set:
            params += param + ','
        nbr_vendeur = len(param_set)
        if nbr_vendeur != 0:
            html = '<a href="{reverse}?id__in={params}">{nbr}</a>'
            html_ = format_html(html.format(reverse=reverse('admin:vendeur_vendeur_changelist'),
                                            nbr=nbr_vendeur, params=params[:-1]))
            return html_
        return 0

    get_nbr_vendeurs.short_description = 'Nbr de Vendeurs'
    get_nbr_vendeurs.allow_tags = True

    def get_fields(self, request, obj=None):
        fields = super(GroupeDeProduitAdmin, self).get_fields(request, obj)
        try:
            groups_list = list(request.user.groups.values_list('name', flat=True))
            if 'Marketing Team' in groups_list:
                fields = ('titre_groupe_de_produit',)
            else:
                fields = ['titre_groupe_de_produit', 'lien_groupe_de_produit',
                          'meta_description_groupe_de_produit',
                          'h1_groupe_de_produit',
                          'paragraphe_groupe_de_produit', 'referencer_groupe_de_produit']
        except IndexError:
            pass
        return fields


class StyleAdmin(admin.ModelAdmin):
    list_display = ('titre_style', 'get_nbr_produit', 'referencer_style', 'utilisateur')
    list_display_links = ('titre_style',)
    list_editable = ('referencer_style', 'utilisateur')
    list_filter = ('referencer_style', 'utilisateur')
    ordering = ('-pk',)
    search_fields = ('titre_style',)

    def get_nbr_produit(self, obj):
        vendeur_categorie = VendeurCategorie.objects.filter(style=obj.pk)
        params = ''
        param_set = set()
        for vendeur in vendeur_categorie:
            try:
                pk_produits = vendeur.produit.all().values_list('pk', flat=True)[0]
                param_set.add(str(pk_produits))
            except IndexError:
                continue
        for param in param_set:
            params += param + ','
        nbr_vendeur = len(param_set)
        if nbr_vendeur != 0:
            html = '<a href="{reverse}?id__in={params}">{nbr}</a>'
            html_ = format_html(html.format(reverse=reverse('admin:vendeur_produit_changelist'),
                                            nbr=nbr_vendeur, params=params[:-1]))
            return html_
        return 0

    get_nbr_produit.short_description = 'Nbr de Tags'
    get_nbr_produit.allow_tags = True

    def get_fields(self, request, obj=None):
        fields = super(StyleAdmin, self).get_fields(request, obj)
        try:
            groups_list = list(request.user.groups.values_list('name', flat=True))
            if 'Marketing Team' in groups_list:
                fields = ('titre_style',)
            else:
                fields = ['titre_style', 'lien_style',
                          'meta_description_style',
                          'h1_style',
                          'paragraphe_style', 'referencer_style']
        except IndexError:
            pass
        return fields


class CibleAdmin(admin.ModelAdmin):
    list_display = ('name_cible',)
    search_fields = ('name_cible',)
    ordering = ('name_cible',)

    def get_model_perms(self, request):
        return {}


admin.site.register(Produit, ProduitAdmin)
admin.site.register(GroupeDeProduit, GroupeDeProduitAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Vendeur, VendeurAdmin)
admin.site.register(Cible, CibleAdmin)


class VendeurCategorieAdmin(admin.ModelAdmin):
    search_fields = ('vendeur',)

    def get_model_perms(self, request):
        return {}


admin.site.register(VendeurCategorie, VendeurCategorieAdmin)

from django.contrib import admin
from .models import Seller, Product, Collection, SousCategories, \
    Categories, Cities, Cible, OfferType, Colors
from django.contrib.admin import ModelAdmin
from django.urls import reverse
from django.utils.html import format_html
from more_admin_filters import MultiSelectDropdownFilter


@admin.action(description="Appliquer <Non contacté> sur les Vendeurs sélectionnés")
def non_contacte(modeladmin, request, queryset):
    queryset.update(seller_status='NC')


@admin.action(description="Appliquer <Non inscrit> sur les Vendeurs sélectionnés")
def non_inscrit(modeladmin, request, queryset):
    queryset.update(seller_status='NI')


@admin.action(description="Appliquer <Pas de réponse> sur les Vendeurs sélectionnés")
def pas_de_reponse(modeladmin, request, queryset):
    queryset.update(seller_status='PR')


@admin.action(description="Appliquer <Gratuit> sur les Vendeurs sélectionnés")
def gratuit(modeladmin, request, queryset):
    queryset.update(seller_status='GR')


@admin.action(description="Appliquer <Payant> sur les Vendeurs sélectionnés")
def payant(modeladmin, request, queryset):
    queryset.update(seller_status='PA')


@admin.action(description="Appliquer <Traiter> sur les Vendeurs sélectionnés")
def traiter(modeladmin, request, queryset):
    queryset.update(processed_status=True)


@admin.action(description="Appliquer <Pipass> sur les Vendeurs sélectionnés")
def pipass(modeladmin, request, queryset):
    queryset.update(pipass=True)


class CustomSellerAdmin(ModelAdmin):
    change_form_template = 'custom_change_form.html'
    list_display = ('seller_name', 'get_seller_link',
                    'get_city_fr', 'number_of_products',
                    'seller_status', 'seller_type', 'processed_status', 'pipass', 'voir')
    search_fields = ('seller_name', 'seller_link', 'city__city_fr')
    list_filter = ('seller_status', 'seller_type', 'processed_status', 'pipass')
    list_editable = ('seller_status', 'seller_type', 'processed_status', 'pipass')
    # list_display_links = ('seller_name',)
    ordering = ('-pk',)
    autocomplete_fields = ['city']
    date_hierarchy = 'created_date'
    actions = [non_contacte, non_inscrit, pas_de_reponse, gratuit, payant, traiter, pipass]

    def get_city_fr(self, obj):
        try:
            return obj.city.city_fr
        except AttributeError:
            return ''

    get_city_fr.admin_order_field = 'city'
    get_city_fr.short_description = 'Ville'

    def get_seller_link(self, obj):
        return format_html(
            '<a href="{0}" target="_blank">{1}</a>', obj.seller_link, obj.seller_link
        )

    get_seller_link.short_description = 'Coordonnées du vendeur'
    get_seller_link.allow_tags = True

    def voir(self, obj):
        return format_html(
            '<a class="changelink" href="{0}{1}/change/">Modifier</a>',
            reverse('admin:seller_seller_changelist'), obj.id
        )

    voir.short_description = 'Actions'
    voir.allow_tags = True

    fieldsets = (
        ('Coordonnées', {
            'classes': ('grp-collapse grp-open',),
            'fields': ('seller_name', 'seller_link', 'city', 'number_of_products'),
        }),
        ('Status', {
            'classes': ('grp-collapse grp-open',),
            'fields': ('processed_status', 'seller_status', 'seller_type', 'pipass'),
        }),
    )

    class StackedItemInline(admin.StackedInline):
        classes = ('grp-collapse grp-open',)

    class TabularItemInline(admin.TabularInline):
        classes = ('grp-collapse grp-open',)


class CustomProductAdmin(ModelAdmin):
    list_display = ('get_seller_name_link', 'product_title', 'price',
                    'show_categories', 'show_sous_categories', 'show_cible',
                    'show_offer_type', 'show_colors', 'show_collections', 'voir')
    search_fields = ('seller__seller_name', 'seller__seller_link',
                     'product_title', 'price', 'category__name_category', 'color__name_color',
                     'collections__collection_name')
    # list_filter = ('category', 'sous_category', 'offer_type', 'color')
    list_filter = [
        ('category__name_category', MultiSelectDropdownFilter),
        ('sous_category__name_sous_category', MultiSelectDropdownFilter),
        ('offer_type__name_offer', MultiSelectDropdownFilter),
        ('color__name_color', MultiSelectDropdownFilter),
    ]
    ordering = ('pk',)
    date_hierarchy = 'created_date'
    # Require model to be registered + custom admin class with the fields in search_fields
    autocomplete_fields = ['category', 'seller', 'cible', 'sous_category',
                           'offer_type', 'color', 'collections']

    def get_seller_name(self, obj):
        return obj.seller.seller_name

    get_seller_name.admin_order_field = 'seller'
    get_seller_name.short_description = 'seller name'

    def get_seller_name_link(self, obj):
        return format_html(
            '<a class="changelink" href="{0}{1}/change/">{2}</a>',
            reverse('admin:seller_seller_changelist'), obj.seller.id, obj.seller.seller_name
        )

    get_seller_name_link.short_description = 'Vendeur'
    get_seller_name_link.allow_tags = True

    def voir(self, obj):
        return format_html(
            '<a class="changelink" href="{0}{1}/change/">Modifier</a>',
            reverse('admin:seller_product_changelist'), obj.id
        )

    voir.short_description = 'Actions'
    voir.allow_tags = True

    def show_categories(self, obj):
        return ",\n".join([i.name_category for i in obj.category.all()])

    show_categories.short_description = 'Catégories'

    def show_colors(self, obj):
        return ",\n".join([i.name_color for i in obj.color.all()])

    show_colors.short_description = 'Couleurs'

    def show_sous_categories(self, obj):
        return ",\n".join([i.name_sous_category for i in obj.sous_category.all()])

    show_sous_categories.short_description = 'Sous catégories'

    def show_cible(self, obj):
        return ",\n".join([i.name_cible for i in obj.cible.all()])

    show_cible.short_description = 'Cible'

    def show_offer_type(self, obj):
        return ",\n".join([i.name_offer for i in obj.offer_type.all()])

    show_offer_type.short_description = "Type d'offre"

    def show_collections(self, obj):
        return ",\n".join([i.collection_name for i in obj.collections.all()])

    show_collections.short_description = "Collections"

    fieldsets = (
        ('Informations vendeur', {
            'classes': ('grp-collapse grp-open',),
            'fields': ('seller',),
        }),
        ('Informations produit', {
            'classes': ('grp-collapse grp-open',),
            'fields': ('product_title', 'price', 'category',
                       'sous_category', 'cible', 'product_link',
                       'offer_type', 'color'),
        }),
        ('Collections', {
            'classes': ('grp-collapse grp-open',),
            'fields': ('collections',),
        }),
    )

    class StackedItemInline(admin.StackedInline):
        classes = ('grp-collapse grp-open',)

    class TabularItemInline(admin.TabularInline):
        classes = ('grp-collapse grp-open',)


class CustomCategoriesAdmin(ModelAdmin):
    list_display = ('name_category',)
    search_fields = ('name_category',)
    ordering = ('name_category',)
    # list_editable = ('name_category',)
    # list_display_links = ('pk',)

    def get_model_perms(self, request):
        return {}


class CustomSousCategoriesAdmin(ModelAdmin):
    list_display = ('name_sous_category', 'voir')
    search_fields = ('name_sous_category',)
    ordering = ('name_sous_category',)
    list_editable = ('name_sous_category',)
    list_display_links = ('voir',)

    def voir(self, obj):
        return format_html(
            '<a href="{0}{1}/change/">Voir</a>',
            reverse('admin:seller_souscategories_changelist'), obj.id
        )

    voir.short_description = 'Actions'
    voir.allow_tags = True


class CustomCitiesAdmin(ModelAdmin):
    list_display = ('city_fr',)
    search_fields = ('city_fr',)
    ordering = ('city_fr',)

    def get_model_perms(self, request):
        return {}


class CustomCollectionsAdmin(ModelAdmin):
    list_display = ('collection_name', 'h1', 'collection_link', 'voir')
    search_fields = ('collection_name', 'h1', 'collection_link', 'meta_description', 'paragraphe')
    list_display_links = ('collection_name',)
    ordering = ('collection_name',)
    date_hierarchy = 'created_date'

    def voir(self, obj):
        return format_html(
            '<a class="changelink" href="{0}{1}/change/">Modifier</a>',
            reverse('admin:seller_collection_changelist'), obj.id
        )

    voir.short_description = 'Actions'
    voir.allow_tags = True


class CustomCibleAdmin(ModelAdmin):
    list_display = ('name_cible',)
    search_fields = ('name_cible',)
    ordering = ('name_cible',)

    def get_model_perms(self, request):
        return {}


class CustomOfferTypeAdmin(ModelAdmin):
    list_display = ('name_offer',)
    search_fields = ('name_offer',)
    ordering = ('name_offer',)

    def get_model_perms(self, request):
        return {}


class CustomColorsAdmin(ModelAdmin):
    list_display = ('name_color',)
    search_fields = ('name_color',)
    ordering = ('name_color',)

    def get_model_perms(self, request):
        return {}


admin.site.register(Seller, CustomSellerAdmin)
admin.site.register(Categories, CustomCategoriesAdmin)
admin.site.register(Cities, CustomCitiesAdmin)
admin.site.register(Cible, CustomCibleAdmin)
admin.site.register(OfferType, CustomOfferTypeAdmin)
admin.site.register(Colors, CustomColorsAdmin)
admin.site.register(Product, CustomProductAdmin)
admin.site.register(Collection, CustomCollectionsAdmin)
admin.site.register(SousCategories, CustomSousCategoriesAdmin)

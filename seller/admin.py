from django.contrib import admin
from .models import Seller, Product, Collection, SousCategories, \
    Categories, Cities, Cible, OfferType, Colors
from django.contrib.admin import ModelAdmin
from django.urls import reverse
from django.utils.html import format_html


class CustomSellerAdmin(ModelAdmin):
    change_form_template = 'custom_change_form.html'
    list_display = ('pk', 'seller_name', 'get_seller_link',
                    'get_city_fr', 'number_of_products',
                    'seller_status', 'seller_type', 'processed_status', 'pipass')
    search_fields = ('pk', 'seller_name', 'seller_link', 'city__city_fr')
    list_filter = ('seller_status', 'seller_type', 'processed_status', 'pipass')
    list_display_links = ('pk', 'seller_name')
    ordering = ('-pk',)
    autocomplete_fields = ['city']

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

    fieldsets = (
        ('Coordonnées', {
            'classes': ('grp-collapse grp-open',),
            'fields': ('seller_name', 'seller_link', 'city', 'number_of_products'),
        }),
        ('Status', {
            'classes': ('grp-collapse grp-open',),
            'fields': ('processed_status', 'seller_status', 'seller_type',),
        }),
    )

    class StackedItemInline(admin.StackedInline):
        classes = ('grp-collapse grp-open',)

    class TabularItemInline(admin.TabularInline):
        classes = ('grp-collapse grp-open',)


class CustomProductAdmin(ModelAdmin):
    list_display = ('pk', 'get_seller_name_link', 'product_title', 'price',
                    'show_categories', 'show_sous_categories', 'show_cible',
                    'show_offer_type', 'show_colors', 'show_collections')
    search_fields = ('pk', 'seller__seller_name', 'seller__seller_link',
                     'product_title', 'price', 'category__name_category', 'color__name_color',
                     'collections__collection_name')
    list_filter = ('category', 'sous_category', 'offer_type', 'color')
    ordering = ('-pk', 'seller')
    # Require model to be registered + custom admin class with the fields in search_fields
    autocomplete_fields = ['category', 'seller', 'cible', 'sous_category',
                           'offer_type', 'color', 'collections']

    def get_seller_name(self, obj):
        return obj.seller.seller_name

    get_seller_name.admin_order_field = 'seller'
    get_seller_name.short_description = 'seller name'

    def get_seller_name_link(self, obj):
        return format_html(
            '<a class="grp-button" href="{0}{1}/change/">{2}</a>',
            reverse('admin:seller_seller_changelist'), obj.seller.id, obj.seller.seller_name
        )

    get_seller_name_link.short_description = 'Vendeur'
    get_seller_name_link.allow_tags = True

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
    list_display = ('pk', 'name_category')
    search_fields = ('pk', 'name_category')
    ordering = ('name_category',)

    def get_model_perms(self, request):
        return {}


class CustomSousCategoriesAdmin(ModelAdmin):
    list_display = ('pk', 'name_sous_category')
    search_fields = ('pk', 'name_sous_category')
    ordering = ('name_sous_category',)


class CustomCitiesAdmin(ModelAdmin):
    list_display = ('pk', 'city_fr')
    search_fields = ('pk', 'city_fr')
    ordering = ('city_fr',)

    def get_model_perms(self, request):
        return {}


class CustomCollectionsAdmin(ModelAdmin):
    list_display = ('pk', 'collection_name', 'h1', 'collection_link')
    search_fields = ('pk', 'collection_name', 'h1', 'collection_link', 'meta_description', 'paragraphe')
    list_display_links = ('pk', 'collection_name')
    ordering = ('collection_name',)


class CustomCibleAdmin(ModelAdmin):
    list_display = ('pk', 'name_cible')
    search_fields = ('pk', 'name_cible')
    ordering = ('name_cible',)

    def get_model_perms(self, request):
        return {}


class CustomOfferTypeAdmin(ModelAdmin):
    list_display = ('pk', 'name_offer')
    search_fields = ('pk', 'name_offer')
    ordering = ('name_offer',)

    def get_model_perms(self, request):
        return {}


class CustomColorsAdmin(ModelAdmin):
    list_display = ('pk', 'name_color')
    search_fields = ('pk', 'name_color')
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

from django.contrib import admin
from .models import Category, Product, Store


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'user')
    list_filter = ('status',)
    list_editable = ('status',)
    search_fields = ('name',)
    actions = ('make_confirmed',)

    def make_confirmed(self, request, queryset):
        rows = queryset.update(status='confirmed')
        self.message_user(request, f'{rows} Updated')
    make_confirmed.short_description = 'Make selected confirmed'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available')
    list_filter = ('available', 'created')
    list_editable = ('price',)
    prepopulated_fields = {'slug': ('name',)}
    # raw_id_fields = ('category',)
    actions = ('make_available',)

    def make_available(self, request, queryset):
        rows = queryset.update(available=True)
        self.message_user(request, f'{rows} Updated')
    make_available.short_description = 'make all available'




from django.contrib import admin

from .models import CheckoutSettings, Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'phone_number',
        'city',
        'created_at',
        'paid',
    )
    list_filter = ('paid', 'created_at')
    search_fields = ('first_name', 'last_name', 'phone_number', 'city')
    readonly_fields = ('created_at',)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'price', 'quantity')
    search_fields = ('order__id', 'product__title')


@admin.register(CheckoutSettings)
class CheckoutSettingsAdmin(admin.ModelAdmin):
    list_display = ('default_whatsapp_number', 'updated_at')

    def has_add_permission(self, request):
        if CheckoutSettings.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False

from django.contrib import admin
from .models import Item, OrderItem, Order, BilingAddress, UserProfile, Payment, CheckZipcode, WishlistedItem, Wishlish, DiscountCode
# Register your models here.
admin.site.register(OrderItem)
admin.site.register(UserProfile)
admin.site.register(WishlistedItem)
admin.site.register(Wishlish)


class BilingAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'country', 'zipcode', 'address_type')

admin.site.register(BilingAddress, BilingAddressAdmin)


class ItemDisplayAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'list_on_frontpage')
    list_filter = ('category',)
    search_fields = ('title', 'category', 'description', 'slug')

admin.site.register(Item, ItemDisplayAdmin)


class PaymentAdminDisplay(admin.ModelAdmin):
    list_display = ('user', 'stripe_charge_id', 'amount')
    search_fields = ('user__username', 'stripe_charge_id')

admin.site.register(Payment, PaymentAdminDisplay)


class OrderAdminDisplay(admin.ModelAdmin):
    list_display = ('user', 'ordered', 'billing_address')

admin.site.register(Order, OrderAdminDisplay)


class CheckZipcodeForDelivery(admin.ModelAdmin):
    search_fields = ('zipcode',)

admin.site.register(CheckZipcode, CheckZipcodeForDelivery)


class DiscountCodeAdmin(admin.ModelAdmin):
    list_display = ('promo_code', 'description')
    search_fields = ('promo_code',)

admin.site.register(DiscountCode, DiscountCodeAdmin)
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import User,Seller,Region,Buyer

# admin.site.register(User, UserAdmin)
# admin.site.register(Seller)
# admin.site.register(Buyer)
# admin.site.register(Region)

from django.contrib import admin
from .models import User, Region, Seller, Buyer, EmailDevice
# Register your models here

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'contact_number', 'address', 'is_seller', 'is_buyer','is_admin','created_at']
    list_filter = ['is_seller', 'is_buyer']
    search_fields = ['username', 'email']

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['user', 'agency_name', 'subscription_status']
    list_filter = ['subscription_status']
    search_fields = ['user__username', 'agency_name']

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ['user']

@admin.register(EmailDevice)
class EamilDeviceAdmin(admin.ModelAdmin):
    list_display = ['email', 'token', 'created_at', 'is_active']



from django.contrib import admin
from .models import Inventory

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "quantity")
    search_fields = ("name",)

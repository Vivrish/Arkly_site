from django.contrib import admin
from .models import Item, Stock


class ItemInLine(admin.StackedInline):
    model = Item
    extra = 3


class StockAdmin(admin.ModelAdmin):
    inlines = [ItemInLine]


class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Visible by user', {'fields': ['name', 'price', 'relevance', 'date', 'description', 'image', 'type', 'size']}),
        ('Invisible by user', {'fields': ['stock', 'slug', 'quantity', 'is_available'], 'classes': ['collapse']})
    ]


admin.site.register(Item, ItemAdmin)
admin.site.register(Stock, StockAdmin)
# Register your models here.

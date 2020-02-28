from django.contrib import admin
from .models import Candle, Scent

@admin.register(Scent)
class ScentAdmin(admin.ModelAdmin):
    exclude = ('favorited_by',)
    list_display = ("name",)

@admin.register(Candle)
class CandleAdmin(admin.ModelAdmin):
    list_display = ("name", "style")



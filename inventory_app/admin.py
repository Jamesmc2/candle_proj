from django.contrib import admin
from .models import Candle

@admin.register(Candle)
class CandleAdmin(admin.ModelAdmin):
    exclude = ('favorited_by',)

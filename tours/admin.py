from django.contrib import admin
from .models import Tour, DailyCity

class DailyCityInline(admin.TabularInline):
    model = DailyCity
    extra = 1  # Varsayılan boş satır sayısı
    fields = ('day_number', 'city', 'description')  # Görünen alanlar

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'guide')
    inlines = [DailyCityInline]

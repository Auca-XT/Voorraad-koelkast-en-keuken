from django.contrib import admin

from .models import Stock

from .forms import stockCreateForm

class StockCreateAdmin(admin.ModelAdmin):
  list_display = ['category', 'item_name', 'quantity']
  form = stockCreateForm
  list_filter = ['category']
  search_fields = ['category', 'item_name']

admin.site.register(Stock, StockCreateAdmin)


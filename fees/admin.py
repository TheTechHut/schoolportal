from django.contrib import admin
from .models import Fees

# Register your models here.

@admin.register(Fees)
class FeesAdmin(admin.ModelAdmin):
    list_display = ['name', 'amount', 'paid']
    list_filter = ['name', 'amount']


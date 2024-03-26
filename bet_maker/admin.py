from django.contrib import admin
from .models import Bets

# Register your models here.
@admin.register(Bets)
class BetsAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'status')
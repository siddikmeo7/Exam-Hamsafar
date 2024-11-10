from django.contrib import admin
from .models import *

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('user','name','start_location','end_location','date_run',)
    search_fields = ('name','end_location','price',)
    list_filter = ('price','start_location','end_location',)

from django.contrib import admin
from .models import House

# Register your models here.

class HouseProfile(admin.ModelAdmin):

    readonly_fields = ('created_at',)
    list_display = ('block_number', 'lot_number', 'owner',)
    search_fields = ('block_number', 'lot_number', 'owner__fname', 'owner__lname') #searching through foreignkey via owner firstname

admin.site.register(House, HouseProfile)



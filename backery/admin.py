from django.contrib import admin

# Register your models here.
@admin.register(Cakes)
class CakesAdmin(admin.ModelAdmin):
    '''Admin View for Cakes'''

    list_display = ('name','descriptions','price','created_onn')
@admin.register(Buiscuit)
class BuiscuitAdmin(admin.ModelAdmin):
    '''Admin View for Buiscuit'''

    list_display = ('name','taste','price','created_on')
    

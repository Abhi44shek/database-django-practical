from django.contrib import admin
from .models import *

# Register your models here.
# adminview shortcut
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','category','pub_date')

# Register your models here.

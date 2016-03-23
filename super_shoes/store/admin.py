from django.contrib import admin
from models import Store


class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
admin.site.register(Store, StoreAdmin)

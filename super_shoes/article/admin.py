from django.contrib import admin
from models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'total_in_shelf', "total_in_vault", "store")
admin.site.register(Article, ArticleAdmin)

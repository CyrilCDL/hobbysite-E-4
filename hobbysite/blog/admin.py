from django.contrib import admin
from .models import Article, ArticleCategory




class ArticleInline(admin.TabularInline):
    model = Article



class ArticleAdmin(admin.ModelAdmin):
    model = Article
    inlines = [ArticleInline]


# Register your models here.
admin.site.register(Article)
admin.site.register(ArticleCategory, ArticleAdmin)

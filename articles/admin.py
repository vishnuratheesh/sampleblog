from django.contrib import admin
from articles.models import Article, Category

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    
    
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
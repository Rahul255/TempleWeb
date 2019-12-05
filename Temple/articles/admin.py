from django.contrib import admin

from . import models

class CommentInline(admin.StackedInline):
    model = models.Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

class PoojaInline(admin.StackedInline):
    model = models.Print
    
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Comment)
admin.site.register(models.Print)
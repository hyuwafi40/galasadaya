from django.contrib import admin
from blog.admin.base import BaseAdminMixin
from blog.models.article import Article


@admin.register(Article)
class ArticleAdmin(BaseAdminMixin, admin.ModelAdmin):
    list_display = ("title", "category", "status", "created_at", "updated_at")
    list_filter = ("status", "category")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ("category", "tags")
    list_select_related = ("category", "created_by")

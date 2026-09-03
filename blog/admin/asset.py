from django.contrib import admin
from blog.admin.base import BaseAdminMixin
from blog.models.asset import Category, Tag


@admin.register(Category)
class CategoryAdmin(BaseAdminMixin, admin.ModelAdmin):
    list_display = ("name", "slug", "created_at", "updated_at")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Tag)
class TagAdmin(BaseAdminMixin, admin.ModelAdmin):
    list_display = ("name", "slug", "created_at", "updated_at")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}

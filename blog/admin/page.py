from django.contrib import admin
from blog.admin.base import BaseAdminMixin
from blog.models.page import Page


@admin.register(Page)
class PageAdmin(BaseAdminMixin, admin.ModelAdmin):
    list_display = ("title", "status", "created_at", "updated_at")
    list_filter = ("status",)
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}

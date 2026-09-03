from django.contrib import admin
from blog.admin.base import BaseAdminMixin
from blog.models.gallery import Album, Photos


@admin.register(Album)
class AlbumAdmin(BaseAdminMixin, admin.ModelAdmin):
    list_display = ("title", "status", "created_at", "updated_at")
    list_filter = ("status",)
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Photos)
class PhotosAdmin(BaseAdminMixin, admin.ModelAdmin):
    list_display = ("id", "album", "category", "created_at")
    list_filter = ("category",)
    search_fields = ("caption",)
    autocomplete_fields = ("album", "category", "tags")
    list_select_related = ("album", "category", "created_by")

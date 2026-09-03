from django.contrib import admin
from blog.admin.base import BaseAdminMixin
from blog.models.advertisement import Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(BaseAdminMixin, admin.ModelAdmin):
    list_display = (
        "name",
        "advertisement_type",
        "ordering",
        "status",
        "end_date",
        "created_at",
    )
    list_filter = ("advertisement_type", "status")
    search_fields = ("name",)

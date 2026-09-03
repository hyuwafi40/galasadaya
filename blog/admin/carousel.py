from django.contrib import admin
from blog.admin.base import BaseAdminMixin
from blog.models.carousel import Carousel


@admin.register(Carousel)
class CarouselAdmin(BaseAdminMixin, admin.ModelAdmin):
    list_display = ("name", "ordering", "created_at", "updated_at")
    search_fields = ("name",)

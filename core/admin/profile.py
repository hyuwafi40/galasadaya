from django.contrib import admin
from core.admin.base import BaseAdminMixin
from core.models.profile import Profile
from core.services import set_verifier


@admin.register(Profile)
class ProfileAdmin(BaseAdminMixin, admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "status",
        "verified_by",
        "verified_at",
        "created_at",
    )
    list_filter = ("status", "gender")
    search_fields = (
        "first_name",
        "last_name",
        "nik",
        "registered_number",
        "email",
        "stage_name",
    )
    readonly_fields = ("verified_by", "verified_at", "created_at", "updated_at")

    def save_model(self, request, obj, form, change):
        if obj.status == "terverifikasi":
            set_verifier(obj, request.user)
        super().save_model(request, obj, form, change)

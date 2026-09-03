from django.contrib import admin


class BaseAdminMixin:
    list_display = ("__str__", "created_by", "created_at", "updated_at")
    readonly_fields = ("created_by", "created_at", "updated_at")

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

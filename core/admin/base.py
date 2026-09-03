from django.contrib import admin


class BaseAdminMixin:
    readonly_fields = ("created_at",)

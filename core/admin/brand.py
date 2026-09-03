from django.contrib import admin
from solo.admin import SingletonModelAdmin
from core.admin.base import BaseAdminMixin
from core.models.brand import Brand


@admin.register(Brand)
class BrandAdmin(BaseAdminMixin, SingletonModelAdmin):
    pass

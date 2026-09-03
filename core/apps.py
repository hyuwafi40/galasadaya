from django.apps import AppConfig
from django.conf import settings
from django.db.models.signals import post_migrate


def create_default_site(sender, **kwargs):
    from django.contrib.sites.models import Site

    site, created = Site.objects.get_or_create(
        id=1,
        defaults={
            "domain": settings.SITE_DOMAIN,
            "name": settings.SITE_NAME,
        },
    )
    if not created:
        site.domain = settings.SITE_DOMAIN
        site.name = settings.SITE_NAME
        site.save()


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"

    def ready(self):
        post_migrate.connect(create_default_site)

from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.conf import settings


def create_default_site(sender, **kwargs):
    from django.contrib.sites.models import Site

    site = Site.objects.filter(id=1).first()
    if not site:
        Site.objects.create(id=1, domain=settings.SITE_DOMAIN, name=settings.SITE_NAME)
    else:
        site.domain = settings.SITE_DOMAIN
        site.name = settings.SITE_NAME
        site.save()


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"

    def ready(self):
        post_migrate.connect(create_default_site)

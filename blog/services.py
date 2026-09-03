from django.utils.text import slugify
from django.db import transaction
import bleach


def generate_unique_slug(model_class, title, instance_pk=None):
    base_slug = slugify(title)
    slug = base_slug
    num = 1
    with transaction.atomic():
        while model_class.objects.filter(slug=slug).exclude(pk=instance_pk).exists():
            slug = f"{base_slug}-{num}"
            num += 1
    return slug


def clean_html(value):
    return bleach.clean(
        value,
        tags=[
            "p",
            "br",
            "strong",
            "em",
            "u",
            "h2",
            "h3",
            "h4",
            "ul",
            "ol",
            "li",
            "a",
            "img",
        ],
        attributes={
            "a": ["href", "title", "target", "rel"],
            "img": ["src", "alt", "width", "height"],
        },
        protocols=["http", "https", "mailto"],
    )

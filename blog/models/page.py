from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from blog.constants import StatusChoices
from blog.models.base import BaseModel
from blog.managers import PublishedManager
from blog.services import generate_unique_slug, clean_html
from blog.validators import validate_url


class Page(BaseModel):
    title = models.CharField(max_length=200)
    thumbnail = models.URLField(validators=[validate_url], blank=True, null=True)
    content = CKEditor5Field()
    status = models.CharField(
        max_length=20, choices=StatusChoices.choices, default=StatusChoices.DRAFT
    )
    slug = models.SlugField(unique=True, max_length=220)

    objects = models.Manager()
    published = PublishedManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(Page, self.title)
        self.content = clean_html(self.content)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]

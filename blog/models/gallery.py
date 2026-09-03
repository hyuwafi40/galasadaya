from django.db import models
from blog.constants import StatusChoices
from blog.models.base import BaseModel
from blog.models.asset import Category, Tag
from blog.managers import PublishedManager
from blog.services import generate_unique_slug
from blog.validators import validate_url


class Album(BaseModel):
    title = models.CharField(max_length=200)
    thumbnail = models.URLField(validators=[validate_url], blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20, choices=StatusChoices.choices, default=StatusChoices.DRAFT
    )
    slug = models.SlugField(unique=True, max_length=220)

    objects = models.Manager()
    published = PublishedManager()

    def save(self, *args, **kwargs):
        self.slug = generate_unique_slug(
            self.__class__, self.slug or self.title, instance_pk=self.pk
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]


class Photos(BaseModel):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="photos")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="photos",
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="photos")
    image = models.URLField(validators=[validate_url])
    caption = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Photo {self.pk} in {self.album.title}"

    class Meta:
        ordering = ["-created_at"]

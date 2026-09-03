from django.db import models
from django.db.models import Q
from django.utils import timezone
from blog.constants import AdvertisementTypeChoices
from blog.models.base import BaseModel
from blog.validators import validate_url


class Advertisement(BaseModel):
    name = models.CharField(max_length=100)
    advertisement_type = models.CharField(
        max_length=50, choices=AdvertisementTypeChoices.choices
    )
    ordering = models.PositiveIntegerField(default=0)
    end_date = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=True)
    image_preview = models.URLField(validators=[validate_url], blank=True, null=True)
    link = models.URLField(validators=[validate_url], blank=True, null=True)

    objects = models.Manager()
    active = models.Manager()

    class Meta:
        ordering = ["ordering", "name"]

    def __str__(self):
        return self.name

    @classmethod
    def active_ads(cls):
        today = timezone.now().date()
        return (
            cls.objects.filter(status=True)
            .filter(Q(end_date__gte=today) | Q(end_date__isnull=True))
            .order_by("ordering")
        )

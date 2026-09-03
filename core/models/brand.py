from django.db import models
from solo.models import SingletonModel
from core.models.base import BaseModel
from core.validators import validate_url


class Brand(BaseModel, SingletonModel):
    name = models.CharField(max_length=200, default="Brand")
    logo = models.URLField(validators=[validate_url], blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    facebook = models.URLField(validators=[validate_url], blank=True, null=True)
    youtube = models.URLField(validators=[validate_url], blank=True, null=True)
    tiktok = models.URLField(validators=[validate_url], blank=True, null=True)
    instagram = models.URLField(validators=[validate_url], blank=True, null=True)

    def __str__(self):
        return self.name

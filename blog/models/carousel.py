from django.db import models
from blog.models.base import BaseModel
from blog.validators import validate_url


class Carousel(BaseModel):
    name = models.CharField(max_length=100)
    image = models.URLField(validators=[validate_url])
    ordering = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["ordering", "name"]

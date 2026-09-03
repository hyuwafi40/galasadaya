from django.conf import settings
from django.db import models
from django.utils import timezone
from core.constants import GenderChoices, ProfileStatusChoices
from core.models.base import BaseModel
from core.managers import VerifiedManager
from core.validators import validate_url


class Profile(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nik = models.CharField(max_length=50, unique=True)
    email = models.EmailField(blank=True, null=True)
    photo_close_up = models.URLField(validators=[validate_url], blank=True, null=True)
    photo_selfie = models.URLField(validators=[validate_url], blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    birth_place = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(
        max_length=20, choices=GenderChoices.choices, blank=True, null=True
    )
    address = models.TextField(blank=True, null=True)
    whatsapp = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    stage_name = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.URLField(validators=[validate_url], blank=True, null=True)
    instagram = models.URLField(validators=[validate_url], blank=True, null=True)
    tiktok = models.URLField(validators=[validate_url], blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    registered_number = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=ProfileStatusChoices.choices,
        default=ProfileStatusChoices.REGISTERED,
    )
    song_1 = models.CharField(max_length=200, blank=True, null=True)
    song_2 = models.CharField(max_length=200, blank=True, null=True)
    verified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        editable=False,
        related_name="verified_profiles",
    )
    verified_at = models.DateTimeField(blank=True, null=True, editable=False)

    objects = models.Manager()
    verified = VerifiedManager()

    _verifier = None

    def save(self, *args, **kwargs):
        if self.status == ProfileStatusChoices.VERIFIED:
            self.verified_at = timezone.now()
            if self._verifier:
                self.verified_by = self._verifier
        else:
            self.verified_by = None
            self.verified_at = None
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

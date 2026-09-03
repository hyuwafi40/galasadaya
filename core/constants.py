from django.db import models


class GenderChoices(models.TextChoices):
    MALE = "Laki-laki", "Laki-laki"
    FEMALE = "Perempuan", "Perempuan"


class ProfileStatusChoices(models.TextChoices):
    REGISTERED = "terdaftar", "Terdaftar"
    VERIFIED = "terverifikasi", "Terverifikasi"

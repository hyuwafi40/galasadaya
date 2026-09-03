from django.db import models


class VerifiedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="terverifikasi")

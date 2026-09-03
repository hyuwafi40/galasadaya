from django.db import models


class StatusChoices(models.TextChoices):
    DRAFT = "draft", "Draft"
    PUBLISHED = "published", "Published"


class AdvertisementTypeChoices(models.TextChoices):
    SKYSCRAPER = "skyscraper", "Skyscraper"
    LEADERBOARD = "leaderboard", "Leaderboard"
    BANNER = "banner", "Banner"
    SQUARE = "square", "Square"

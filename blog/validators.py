from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def validate_url(value):
    url_validator = URLValidator(schemes=["http", "https"])
    try:
        url_validator(value)
    except ValidationError:
        raise ValidationError("Enter a valid URL.")

import re
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.utils.translation import gettext as _


class ComplexityValidator:
    def validate(self, password, user=None):
        if not re.search(r"[A-Z]", password):
            raise ValidationError(
                _("Password harus mengandung minimal satu huruf besar.")
            )
        if not re.search(r"[a-z]", password):
            raise ValidationError(
                _("Password harus mengandung minimal satu huruf kecil.")
            )
        if not re.search(r"\d", password):
            raise ValidationError(_("Password harus mengandung minimal satu angka."))
        if not re.search(r"[^A-Za-z0-9]", password):
            raise ValidationError(_("Password harus mengandung minimal satu simbol."))

    def get_help_text(self):
        return _(
            "Password harus mengandung kombinasi huruf besar, huruf kecil, angka, dan simbol."
        )


def validate_url(value):
    url_validator = URLValidator(schemes=["http", "https"])
    try:
        url_validator(value)
    except ValidationError:
        raise ValidationError("Enter a valid URL.")

from django import forms
from blog.models.carousel import Carousel
from core.forms.base import BaseFormMixin


class CarouselForm(BaseFormMixin, forms.ModelForm):
    class Meta:
        model = Carousel
        fields = ["name", "image", "ordering"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs["placeholder"] = "Nama carousel"
        self.fields["image"].widget.attrs[
            "placeholder"
        ] = "https://example.com/image.jpg"
        self.fields["ordering"].widget.attrs["placeholder"] = "0"

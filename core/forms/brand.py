from django import forms
from core.models.brand import Brand
from core.forms.base import BaseFormMixin


class BrandForm(BaseFormMixin, forms.ModelForm):
    class Meta:
        model = Brand
        fields = [
            "name",
            "logo",
            "description",
            "facebook",
            "youtube",
            "tiktok",
            "instagram",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs["placeholder"] = "Nama brand"
        self.fields["logo"].widget.attrs["placeholder"] = "https://example.com/logo.png"
        self.fields["description"].widget.attrs[
            "placeholder"
        ] = "Deskripsi singkat brand"
        self.fields["facebook"].widget.attrs["placeholder"] = "https://facebook.com/..."
        self.fields["youtube"].widget.attrs["placeholder"] = "https://youtube.com/..."
        self.fields["tiktok"].widget.attrs["placeholder"] = "https://tiktok.com/..."
        self.fields["instagram"].widget.attrs[
            "placeholder"
        ] = "https://instagram.com/..."

from django import forms
from blog.models.gallery import Album, Photos
from core.forms.base import BaseFormMixin


class AlbumForm(BaseFormMixin, forms.ModelForm):
    class Meta:
        model = Album
        fields = ["title", "thumbnail", "description", "status"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs["placeholder"] = "Judul album"
        self.fields["thumbnail"].widget.attrs[
            "placeholder"
        ] = "https://example.com/cover.jpg"
        self.fields["description"].widget.attrs["placeholder"] = "Deskripsi album"


class PhotoForm(BaseFormMixin, forms.ModelForm):
    class Meta:
        model = Photos
        fields = ["album", "category", "tags", "image", "caption"]

    def __init__(self, *args, **kwargs):
        include_album = kwargs.pop("include_album", True)
        super().__init__(*args, **kwargs)
        if not include_album:
            self.fields.pop("album", None)
        self.fields["image"].widget.attrs[
            "placeholder"
        ] = "https://example.com/photo.jpg"
        self.fields["caption"].widget.attrs["placeholder"] = "Caption foto"

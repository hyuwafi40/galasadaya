from django import forms
from blog.models.asset import Tag
from core.forms.base import BaseFormMixin


class TagForm(BaseFormMixin, forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs["placeholder"] = "Nama tag"

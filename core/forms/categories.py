from django import forms
from blog.models.asset import Category
from core.forms.base import BaseFormMixin


class CategoryForm(BaseFormMixin, forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs["placeholder"] = "Nama kategori"

from django import forms
from blog.models.page import Page
from django_ckeditor_5.widgets import CKEditor5Widget


class PageForm(forms.ModelForm):
    is_published = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={"class": "toggle-switch"})
    )

    class Meta:
        model = Page
        fields = ["title", "thumbnail", "content", "is_published"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "glass-input w-full px-4 py-3 rounded-2xl text-sm font-medium text-slate-800",
                    "placeholder": "Judul halaman",
                }
            ),
            "thumbnail": forms.URLInput(
                attrs={
                    "class": "glass-input w-full px-4 py-3 rounded-2xl text-sm font-medium text-slate-800",
                    "placeholder": "https://example.com/thumb.jpg",
                }
            ),
            "content": CKEditor5Widget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields["is_published"].initial = self.instance.status == "published"

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.status = (
            "published" if self.cleaned_data.get("is_published") else "draft"
        )
        if commit:
            instance.save()
        return instance

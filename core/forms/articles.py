from django import forms
from blog.models.article import Article
from django_ckeditor_5.widgets import CKEditor5Widget


class ArticleForm(forms.ModelForm):
    is_published = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={"class": "toggle-switch"})
    )

    class Meta:
        model = Article
        fields = [
            "title",
            "thumbnail",
            "category",
            "tags",
            "content",
            "excerpt",
            "is_published",
        ]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "glass-input w-full px-4 py-3 rounded-2xl text-sm font-medium text-slate-800",
                    "placeholder": "Judul artikel",
                }
            ),
            "thumbnail": forms.URLInput(
                attrs={
                    "class": "glass-input w-full px-4 py-3 rounded-2xl text-sm font-medium text-slate-800",
                    "placeholder": "https://example.com/thumb.jpg",
                }
            ),
            "category": forms.Select(
                attrs={
                    "class": "glass-input w-full px-4 py-3 rounded-2xl text-sm font-medium text-slate-800 appearance-none bg-transparent"
                }
            ),
            "tags": forms.CheckboxSelectMultiple(attrs={"class": "tag-checkbox-list"}),
            "content": CKEditor5Widget(),
            "excerpt": forms.Textarea(
                attrs={
                    "rows": 3,
                    "class": "glass-input w-full px-4 py-3 rounded-2xl text-sm font-medium text-slate-800",
                    "placeholder": "Ringkasan singkat artikel",
                }
            ),
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
            self.save_m2m()
        return instance

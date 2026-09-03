from django import forms
from blog.models.advertisement import Advertisement


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = [
            "name",
            "advertisement_type",
            "image_preview",
            "link",
            "ordering",
            "end_date",
            "status",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "glass-input w-full px-4 py-3 rounded-2xl text-sm font-medium text-slate-800",
                    "placeholder": "Nama iklan",
                }
            ),
            "advertisement_type": forms.Select(
                attrs={
                    "class": "glass-input w-full px-4 py-3 rounded-2xl text-sm font-medium text-slate-800 appearance-none bg-transparent"
                }
            ),
            "image_preview": forms.URLInput(
                attrs={
                    "class": "glass-input w-full px-4 py-3 rounded-2xl text-sm font-medium text-slate-800",
                    "placeholder": "https://example.com/preview.jpg",
                }
            ),
            "link": forms.URLInput(
                attrs={
                    "class": "glass-input w-full px-4 py-3 rounded-2xl text-sm font-medium text-slate-800",
                    "placeholder": "https://example.com",
                }
            ),
            "ordering": forms.NumberInput(
                attrs={
                    "class": "glass-input w-full px-4 py-3 rounded-2xl text-sm font-medium text-slate-800",
                    "placeholder": "0",
                }
            ),
            "end_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "glass-input w-full px-4 py-3 rounded-2xl text-sm font-medium text-slate-800",
                }
            ),
            "status": forms.CheckboxInput(attrs={"class": "toggle-switch"}),
        }

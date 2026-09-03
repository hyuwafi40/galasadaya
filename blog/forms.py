from django import forms
from blog.models.comment import Comment
from blog.models.contact import ContactMessage


class ContactForm(forms.ModelForm):
    website = forms.CharField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "glass-input w-full px-5 py-4 rounded-2xl font-bold text-sm",
                    "placeholder": "Nama Lengkap",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "glass-input w-full px-5 py-4 rounded-2xl font-bold text-sm",
                    "placeholder": "Email",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "rows": 5,
                    "class": "glass-input w-full px-5 py-4 rounded-2xl font-bold text-sm resize-none",
                    "placeholder": "Ceritakan tentang karyamu...",
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("website"):
            raise forms.ValidationError("Spam terdeteksi.")
        return cleaned_data


class CommentForm(forms.ModelForm):
    website = forms.CharField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Comment
        fields = ["name", "email", "text"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "glass-input w-full px-5 py-4 rounded-2xl font-bold text-sm",
                    "placeholder": "Nama Lo...",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "glass-input w-full px-5 py-4 rounded-2xl font-bold text-sm",
                    "placeholder": "Email (Ga bakal di-publish)",
                }
            ),
            "text": forms.Textarea(
                attrs={
                    "rows": 3,
                    "class": "glass-input w-full px-5 py-4 rounded-2xl font-bold text-sm resize-none",
                    "placeholder": "Gimana menurut lo event ini?",
                }
            ),
        }

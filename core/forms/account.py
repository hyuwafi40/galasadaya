from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password
from core.forms.base import BaseFormMixin

User = get_user_model()


class UserCreateForm(BaseFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "is_staff", "is_superuser", "is_active"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["placeholder"] = "Username"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password2"].widget.attrs["placeholder"] = "Konfirmasi password"


class UserUpdateForm(BaseFormMixin, forms.ModelForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password baru"}),
        required=False,
        validators=[validate_password],
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Konfirmasi password baru"}),
        required=False,
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_superuser",
            "is_active",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["placeholder"] = "Username"
        self.fields["first_name"].widget.attrs["placeholder"] = "Nama depan"
        self.fields["last_name"].widget.attrs["placeholder"] = "Nama belakang"
        self.fields["email"].widget.attrs["placeholder"] = "Email"

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("new_password1")
        password2 = cleaned_data.get("new_password2")
        if password1 or password2:
            if password1 != password2:
                raise forms.ValidationError("Password baru dan konfirmasi tidak sama.")
        return cleaned_data

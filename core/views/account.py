from django.contrib.auth import get_user_model
from core.forms.account import UserCreateForm, UserUpdateForm
from core.views.base import BaseListView, BaseCreateView, BaseUpdateView, BaseDeleteView

User = get_user_model()


class AccountListView(BaseListView):
    model = User
    template_name = "core/account.html"
    context_object_name = "users"
    ordering = ["-date_joined"]
    htmx_template_name = "core/account/table.html"
    search_fields = ["username", "first_name", "last_name", "email"]
    required_role = "developer"


class AccountCreateView(BaseCreateView):
    template_name = "core/account/form.html"
    form_class = UserCreateForm
    success_url_name = "core:account"
    success_message = "User berhasil dibuat."
    error_message = "Gagal membuat user."
    required_role = "developer"


class AccountUpdateView(BaseUpdateView):
    model = User
    template_name = "core/account/form.html"
    form_class = UserUpdateForm
    success_url_name = "core:account"
    success_message = "User berhasil diperbarui."
    error_message = "Gagal memperbarui user."
    context_object_name = "user"
    required_role = "developer"

    def save_form(self, form):
        user = form.save(commit=False)
        new_password = form.cleaned_data.get("new_password1")
        if new_password:
            user.set_password(new_password)
        user.save()
        return user


class AccountDeleteView(BaseDeleteView):
    model = User
    success_url_name = "core:account"
    success_message = "User berhasil dihapus."
    error_message = "User tidak dapat dihapus."
    required_role = "developer"

    def can_delete(self, request, obj):
        if obj == request.user:
            return False
        if obj.is_superuser and User.objects.filter(is_superuser=True).count() == 1:
            return False
        return True

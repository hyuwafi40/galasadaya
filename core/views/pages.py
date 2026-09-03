from blog.models.page import Page
from core.forms.pages import PageForm
from core.views.base import (
    BaseListView,
    BaseCreateView,
    BaseUpdateView,
    BaseDeleteView,
    BaseStatusUpdateView,
)


class PagesListView(BaseListView):
    model = Page
    template_name = "core/pages.html"
    context_object_name = "pages"
    htmx_template_name = "core/pages/table.html"
    search_fields = ["title", "content"]
    required_role = "administrator"


class PageCreateView(BaseCreateView):
    template_name = "core/pages/form.html"
    form_class = PageForm
    success_url_name = "core:pages"
    success_message = "Halaman berhasil dibuat."
    error_message = "Gagal membuat halaman."
    required_role = "administrator"

    def save_form(self, form):
        page = form.save(commit=False)
        page.created_by = self.request.user
        page.save()
        return page


class PageUpdateView(BaseUpdateView):
    model = Page
    template_name = "core/pages/form.html"
    form_class = PageForm
    success_url_name = "core:pages"
    success_message = "Halaman berhasil diperbarui."
    error_message = "Gagal memperbarui halaman."
    context_object_name = "page"
    required_role = "administrator"


class PageDeleteView(BaseDeleteView):
    model = Page
    success_url_name = "core:pages"
    success_message = "Halaman berhasil dihapus."
    error_message = "Halaman tidak dapat dihapus."
    required_role = "administrator"

    def can_delete(self, request, obj):
        return request.user.is_superuser or obj.created_by_id == request.user.id


class PageStatusUpdateView(BaseStatusUpdateView):
    model = Page
    status_field = "status"
    allowed_values = ("draft", "published")
    success_url_name = "core:pages"
    success_message = "Status halaman diperbarui."
    error_message = "Status tidak valid."
    required_role = "administrator"

    def can_update_status(self, request, obj):
        return request.user.is_superuser or obj.created_by_id == request.user.id

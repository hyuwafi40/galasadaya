from blog.models.asset import Tag
from core.forms.tags import TagForm
from core.views.base import BaseListView, BaseCreateView, BaseUpdateView, BaseDeleteView


class TagsListView(BaseListView):
    model = Tag
    template_name = "core/tags.html"
    context_object_name = "tags"
    htmx_template_name = "core/tags/table.html"
    search_fields = ["name", "slug"]
    required_role = "administrator"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TagForm()
        return context


class TagCreateView(BaseCreateView):
    template_name = "core/tags/form.html"
    form_class = TagForm
    success_url_name = "core:tags"
    success_message = "Tag berhasil dibuat."
    error_message = "Gagal membuat tag."
    required_role = "administrator"


class TagUpdateView(BaseUpdateView):
    model = Tag
    template_name = "core/tags/form.html"
    form_class = TagForm
    success_url_name = "core:tags"
    success_message = "Tag berhasil diperbarui."
    error_message = "Gagal memperbarui tag."
    required_role = "administrator"


class TagDeleteView(BaseDeleteView):
    model = Tag
    success_url_name = "core:tags"
    success_message = "Tag berhasil dihapus."
    error_message = "Tag tidak dapat dihapus."
    required_role = "administrator"

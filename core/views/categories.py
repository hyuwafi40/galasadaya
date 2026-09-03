from blog.models.asset import Category
from core.forms.categories import CategoryForm
from core.views.base import BaseListView, BaseCreateView, BaseUpdateView, BaseDeleteView


class CategoriesListView(BaseListView):
    model = Category
    template_name = "core/categories.html"
    context_object_name = "categories"
    htmx_template_name = "core/categories/table.html"
    search_fields = ["name", "slug"]
    required_role = "administrator"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CategoryForm()
        return context


class CategoryCreateView(BaseCreateView):
    template_name = "core/categories/form.html"
    form_class = CategoryForm
    success_url_name = "core:categories"
    success_message = "Kategori berhasil dibuat."
    error_message = "Gagal membuat kategori."
    required_role = "administrator"


class CategoryUpdateView(BaseUpdateView):
    model = Category
    template_name = "core/categories/form.html"
    form_class = CategoryForm
    success_url_name = "core:categories"
    success_message = "Kategori berhasil diperbarui."
    error_message = "Gagal memperbarui kategori."
    required_role = "administrator"


class CategoryDeleteView(BaseDeleteView):
    model = Category
    success_url_name = "core:categories"
    success_message = "Kategori berhasil dihapus."
    error_message = "Kategori tidak dapat dihapus."
    required_role = "administrator"

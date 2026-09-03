from blog.models.article import Article
from core.forms.articles import ArticleForm
from core.views.base import (
    BaseListView,
    BaseCreateView,
    BaseUpdateView,
    BaseDeleteView,
    BaseStatusUpdateView,
)


class ArticlesListView(BaseListView):
    model = Article
    template_name = "core/articles.html"
    context_object_name = "articles"
    htmx_template_name = "core/articles/table.html"
    search_fields = ["title", "content"]
    required_role = "reguler"


class ArticleCreateView(BaseCreateView):
    template_name = "core/articles/form.html"
    form_class = ArticleForm
    success_url_name = "core:articles"
    success_message = "Artikel berhasil dibuat."
    error_message = "Gagal membuat artikel."
    required_role = "administrator"

    def save_form(self, form):
        article = form.save(commit=False)
        article.created_by = self.request.user
        article.save()
        form.save_m2m()
        return article


class ArticleUpdateView(BaseUpdateView):
    model = Article
    template_name = "core/articles/form.html"
    form_class = ArticleForm
    success_url_name = "core:articles"
    success_message = "Artikel berhasil diperbarui."
    error_message = "Gagal memperbarui artikel."
    context_object_name = "article"
    required_role = "administrator"


class ArticleDeleteView(BaseDeleteView):
    model = Article
    success_url_name = "core:articles"
    success_message = "Artikel berhasil dihapus."
    error_message = "Artikel tidak dapat dihapus."
    required_role = "administrator"

    def can_delete(self, request, obj):
        return request.user.is_superuser or obj.created_by_id == request.user.id


class ArticleStatusUpdateView(BaseStatusUpdateView):
    model = Article
    status_field = "status"
    allowed_values = ("draft", "published")
    success_url_name = "core:articles"
    success_message = "Status artikel diperbarui."
    error_message = "Status tidak valid."
    required_role = "administrator"

    def can_update_status(self, request, obj):
        return request.user.is_superuser or obj.created_by_id == request.user.id

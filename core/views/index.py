from django.contrib.auth import get_user_model
from django.views.generic import TemplateView
from blog.models.article import Article
from blog.models.asset import Category, Tag
from blog.models.gallery import Album, Photos
from blog.models.advertisement import Advertisement
from blog.models.comment import Comment
from blog.models.contact import ContactMessage
from core.views.base import AccessMixin

User = get_user_model()


class IndexView(AccessMixin, TemplateView):
    template_name = "core/index.html"
    required_role = "reguler"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_articles"] = Article.objects.count()
        context["total_articles_published"] = Article.objects.filter(
            status="published"
        ).count()
        context["total_articles_draft"] = Article.objects.filter(status="draft").count()
        context["total_categories"] = Category.objects.count()
        context["total_tags"] = Tag.objects.count()
        context["total_albums"] = Album.objects.count()
        context["total_photos"] = Photos.objects.count()
        context["total_advertisements"] = Advertisement.objects.filter(
            status=True
        ).count()
        context["total_users"] = User.objects.filter(is_staff=True).count()
        context["recent_articles"] = Article.objects.order_by("-created_at")[:5]
        context["recent_comments"] = Comment.objects.order_by("-created_at")[:5]
        context["recent_contacts"] = ContactMessage.objects.order_by("-created_at")[:5]
        return context

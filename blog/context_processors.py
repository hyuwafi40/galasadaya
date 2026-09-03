from blog.models.asset import Category
from blog.models.article import Article
from blog.navbar import NAVBAR_MENUS
from blog.footer import FOOTER_INFO_LINKS, FOOTER_CONFIG


def blog_context(request):
    categories = Category.objects.filter(articles__status="published").distinct()[:5]
    recent_articles = Article.published.all().order_by("-created_at")[:3]
    return {
        "categories": categories,
        "navbar_menus": NAVBAR_MENUS,
        "footer_info_links": FOOTER_INFO_LINKS,
        "footer_config": FOOTER_CONFIG,
        "recent_articles": recent_articles,
    }

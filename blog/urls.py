from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path("", views.ArticleListView.as_view(), name="index"),
    path("articles/", views.ArticleListPageView.as_view(), name="article_list"),
    path("article/<slug:slug>/", views.ArticleDetailView.as_view(), name="article"),
    path(
        "category/<slug:slug>/",
        views.CategoryArticleListView.as_view(),
        name="category",
    ),
    path("tag/<slug:slug>/", views.TagArticleListView.as_view(), name="tag"),
    path("search/", views.SearchView.as_view(), name="search"),
    path("pages/", views.PageListView.as_view(), name="page_list"),
    path("page/<slug:slug>/", views.PageDetailView.as_view(), name="page"),
    path("gallery/", views.AlbumListView.as_view(), name="gallery_list"),
    path(
        "gallery/<slug:slug>/", views.AlbumDetailView.as_view(), name="gallery_detail"
    ),
    path("contact/", views.ContactFormView.as_view(), name="contact"),
    path("robots.txt", views.RobotsView.as_view(), name="robots"),
    path("sitemap.xml", views.SitemapView.as_view(), name="sitemap"),
]

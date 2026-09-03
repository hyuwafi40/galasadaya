from django.urls import path
from core.views import IndexView
from core.views.categories import (
    CategoriesListView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
)
from core.views.tags import TagsListView, TagCreateView, TagUpdateView, TagDeleteView
from core.views.carousels import (
    CarouselsListView,
    CarouselCreateView,
    CarouselUpdateView,
    CarouselDeleteView,
)
from core.views.ads import AdsListView, AdCreateView, AdUpdateView, AdDeleteView
from core.views.brand import BrandView, BrandFormView
from core.views.articles import (
    ArticlesListView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleStatusUpdateView,
)
from core.views.pages import (
    PagesListView,
    PageCreateView,
    PageUpdateView,
    PageDeleteView,
    PageStatusUpdateView,
)
from core.views.account import (
    AccountListView,
    AccountCreateView,
    AccountUpdateView,
    AccountDeleteView,
)
from core.views.galleries import (
    GalleriesView,
    AlbumPhotosView,
    AlbumCreateView,
    AlbumUpdateView,
    AlbumDeleteView,
    AlbumStatusUpdateView,
    PhotoCreateView,
    PhotoUpdateView,
    PhotoDeleteView,
)

app_name = "core"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("cat/", CategoriesListView.as_view(), name="categories"),
    path("cat/cre/", CategoryCreateView.as_view(), name="categories_create"),
    path("cat/<int:pk>/upd/", CategoryUpdateView.as_view(), name="categories_update"),
    path("cat/<int:pk>/del/", CategoryDeleteView.as_view(), name="categories_delete"),
    path("tag/", TagsListView.as_view(), name="tags"),
    path("tag/cre/", TagCreateView.as_view(), name="tags_create"),
    path("tag/<int:pk>/upd/", TagUpdateView.as_view(), name="tags_update"),
    path("tag/<int:pk>/del/", TagDeleteView.as_view(), name="tags_delete"),
    path("car/", CarouselsListView.as_view(), name="carousels"),
    path("car/cre/", CarouselCreateView.as_view(), name="carousels_create"),
    path("car/<int:pk>/upd/", CarouselUpdateView.as_view(), name="carousels_update"),
    path("car/<int:pk>/del/", CarouselDeleteView.as_view(), name="carousels_delete"),
    path("ads/", AdsListView.as_view(), name="ads"),
    path("ads/cre/", AdCreateView.as_view(), name="ads_create"),
    path("ads/<int:pk>/upd/", AdUpdateView.as_view(), name="ads_update"),
    path("ads/<int:pk>/del/", AdDeleteView.as_view(), name="ads_delete"),
    path("brand/", BrandView.as_view(), name="brand"),
    path("brand/form/", BrandFormView.as_view(), name="brand_form"),
    path("art/", ArticlesListView.as_view(), name="articles"),
    path("art/cre/", ArticleCreateView.as_view(), name="articles_create"),
    path("art/<int:pk>/upd/", ArticleUpdateView.as_view(), name="articles_update"),
    path("art/<int:pk>/del/", ArticleDeleteView.as_view(), name="articles_delete"),
    path(
        "art/<int:pk>/status/",
        ArticleStatusUpdateView.as_view(),
        name="articles_status",
    ),
    path("pag/", PagesListView.as_view(), name="pages"),
    path("pag/cre/", PageCreateView.as_view(), name="pages_create"),
    path("pag/<int:pk>/upd/", PageUpdateView.as_view(), name="pages_update"),
    path("pag/<int:pk>/del/", PageDeleteView.as_view(), name="pages_delete"),
    path("pag/<int:pk>/status/", PageStatusUpdateView.as_view(), name="pages_status"),
    path("usr/", AccountListView.as_view(), name="account"),
    path("usr/cre/", AccountCreateView.as_view(), name="account_create"),
    path("usr/<int:pk>/upd/", AccountUpdateView.as_view(), name="account_update"),
    path("usr/<int:pk>/del/", AccountDeleteView.as_view(), name="account_delete"),
    path("gal/", GalleriesView.as_view(), name="galleries"),
    path("gal/alb/cre/", AlbumCreateView.as_view(), name="galleries_album_create"),
    path(
        "gal/alb/<int:pk>/photos/",
        AlbumPhotosView.as_view(),
        name="galleries_album_photos",
    ),
    path(
        "gal/alb/<int:pk>/upd/",
        AlbumUpdateView.as_view(),
        name="galleries_album_update",
    ),
    path(
        "gal/alb/<int:pk>/del/",
        AlbumDeleteView.as_view(),
        name="galleries_album_delete",
    ),
    path(
        "gal/alb/<int:pk>/status/",
        AlbumStatusUpdateView.as_view(),
        name="galleries_album_status",
    ),
    path(
        "gal/alb/<int:album_pk>/pho/cre/",
        PhotoCreateView.as_view(),
        name="galleries_photo_create",
    ),
    path(
        "gal/pho/<int:pk>/upd/",
        PhotoUpdateView.as_view(),
        name="galleries_photo_update",
    ),
    path(
        "gal/pho/<int:pk>/del/",
        PhotoDeleteView.as_view(),
        name="galleries_photo_delete",
    ),
]

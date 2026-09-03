from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.defaults import (
    page_not_found,
    server_error,
    permission_denied,
    bad_request,
)
from config import views

urlpatterns = [
    path("", include("blog.urls", namespace="blog")),
    path("admin/", admin.site.urls),
    path("core/", include("core.urls", namespace="core")),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler400 = bad_request
handler403 = permission_denied
handler404 = page_not_found
handler500 = server_error

from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import TemplateView
from blog.models.gallery import Album, Photos
from core.forms.galleries import AlbumForm, PhotoForm
from core.views.base import (
    AccessMixin,
    BaseCreateView,
    BaseUpdateView,
    BaseDeleteView,
    BaseStatusUpdateView,
)


def paginate_queryset(request, queryset, per_page=10):
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return page_obj


class GalleriesView(AccessMixin, TemplateView):
    template_name = "core/galleries.html"
    required_role = "reguler"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_album = self.request.GET.get("q_album", "").strip()
        album_queryset = Album.objects.annotate(total_photos=Count("photos"))
        if search_album:
            album_queryset = album_queryset.filter(
                Q(title__icontains=search_album)
                | Q(description__icontains=search_album)
            )
        context["albums"] = paginate_queryset(
            self.request, album_queryset.order_by("-created_at")
        )
        context["search_album"] = search_album
        context["total_albums"] = Album.objects.count()
        context["form_album"] = AlbumForm()
        return context

    def get_template_names(self):
        if self.request.htmx:
            return ["core/galleries/table_album.html"]
        return [self.template_name]


class AlbumPhotosView(AccessMixin, TemplateView):
    template_name = "core/galleries/photos.html"
    required_role = "reguler"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        album_pk = self.kwargs.get("pk")
        album = get_object_or_404(Album, pk=album_pk)
        photos_queryset = Photos.objects.filter(album=album).order_by("-created_at")
        context["album"] = album
        context["photos"] = paginate_queryset(self.request, photos_queryset)
        context["total_photos"] = photos_queryset.count()
        context["form_photo"] = PhotoForm(include_album=False)
        return context


class AlbumCreateView(BaseCreateView):
    template_name = "core/galleries/form_album.html"
    form_class = AlbumForm
    success_url_name = "core:galleries"
    success_message = "Album berhasil dibuat."
    error_message = "Gagal membuat album."
    required_role = "administrator"

    def save_form(self, form):
        album = form.save(commit=False)
        album.created_by = self.request.user
        album.save()
        return album


class AlbumUpdateView(BaseUpdateView):
    model = Album
    template_name = "core/galleries/form_album.html"
    form_class = AlbumForm
    success_url_name = "core:galleries"
    success_message = "Album berhasil diperbarui."
    error_message = "Gagal memperbarui album."
    context_object_name = "album"
    required_role = "administrator"


class AlbumDeleteView(BaseDeleteView):
    model = Album
    success_url_name = "core:galleries"
    success_message = "Album dan semua foto di dalamnya berhasil dihapus."
    error_message = "Album tidak dapat dihapus."
    required_role = "administrator"

    def can_delete(self, request, obj):
        return request.user.is_superuser or obj.created_by_id == request.user.id


class AlbumStatusUpdateView(BaseStatusUpdateView):
    model = Album
    status_field = "status"
    allowed_values = ("draft", "published")
    success_url_name = "core:galleries"
    success_message = "Status album diperbarui."
    error_message = "Status tidak valid."
    required_role = "administrator"


class PhotoCreateView(BaseCreateView):
    template_name = "core/galleries/form_photos.html"
    form_class = PhotoForm
    success_message = "Foto berhasil ditambahkan."
    error_message = "Gagal menambahkan foto."
    required_role = "administrator"

    def get_success_url(self):
        return reverse(
            "core:galleries_album_photos", kwargs={"pk": self.kwargs["album_pk"]}
        )

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["include_album"] = False
        return kwargs

    def get(self, request, album_pk):
        self.album = get_object_or_404(Album, pk=album_pk)
        form = PhotoForm(include_album=False)
        return render(request, self.template_name, {"form": form, "album": self.album})

    def post(self, request, album_pk):
        self.album = get_object_or_404(Album, pk=album_pk)
        form = PhotoForm(request.POST, include_album=False)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.album = self.album
            photo.created_by = request.user
            photo.save()
            form.save_m2m()
            messages.success(request, self.success_message)
            return redirect(self.get_success_url())
        messages.error(request, self.error_message)
        return render(request, self.template_name, {"form": form, "album": self.album})


class PhotoUpdateView(BaseUpdateView):
    model = Photos
    template_name = "core/galleries/form_photos.html"
    form_class = PhotoForm
    success_message = "Foto berhasil diperbarui."
    error_message = "Gagal memperbarui foto."
    context_object_name = "photo"
    required_role = "administrator"

    def get_success_url(self):
        return reverse(
            "core:galleries_album_photos", kwargs={"pk": self.object.album_id}
        )

    def get_context_data(self, form, obj=None):
        context = super().get_context_data(form, obj)
        if obj:
            context["album"] = obj.album
        return context


class PhotoDeleteView(BaseDeleteView):
    model = Photos
    success_message = "Foto berhasil dihapus."
    error_message = "Foto tidak dapat dihapus."
    required_role = "administrator"

    def get_success_url(self):
        return reverse(
            "core:galleries_album_photos", kwargs={"pk": self.kwargs["album_pk"]}
        )

    def can_delete(self, request, obj):
        return request.user.is_superuser or obj.created_by_id == request.user.id

    def post(self, request, pk):
        photo = get_object_or_404(Photos, pk=pk)
        self.kwargs["album_pk"] = photo.album_id
        return super().post(request, pk)

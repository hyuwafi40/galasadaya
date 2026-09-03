from blog.models.advertisement import Advertisement
from core.forms.ads import AdvertisementForm
from core.views.base import BaseListView, BaseCreateView, BaseUpdateView, BaseDeleteView


class AdsListView(BaseListView):
    model = Advertisement
    template_name = "core/ads.html"
    context_object_name = "ads"
    htmx_template_name = "core/ads/table.html"
    search_fields = ["name", "advertisement_type", "link"]
    required_role = "administrator"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AdvertisementForm()
        return context


class AdCreateView(BaseCreateView):
    template_name = "core/ads/form.html"
    form_class = AdvertisementForm
    success_url_name = "core:ads"
    success_message = "Iklan berhasil dibuat."
    error_message = "Gagal membuat iklan."
    required_role = "administrator"


class AdUpdateView(BaseUpdateView):
    model = Advertisement
    template_name = "core/ads/form.html"
    form_class = AdvertisementForm
    success_url_name = "core:ads"
    success_message = "Iklan berhasil diperbarui."
    error_message = "Gagal memperbarui iklan."
    required_role = "administrator"


class AdDeleteView(BaseDeleteView):
    model = Advertisement
    success_url_name = "core:ads"
    success_message = "Iklan berhasil dihapus."
    error_message = "Iklan tidak dapat dihapus."
    required_role = "administrator"

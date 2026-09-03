from blog.models.carousel import Carousel
from core.forms.carousels import CarouselForm
from core.views.base import BaseListView, BaseCreateView, BaseUpdateView, BaseDeleteView


class CarouselsListView(BaseListView):
    model = Carousel
    template_name = "core/carousels.html"
    context_object_name = "carousels"
    htmx_template_name = "core/carousels/table.html"
    search_fields = ["name"]
    required_role = "administrator"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CarouselForm()
        return context


class CarouselCreateView(BaseCreateView):
    template_name = "core/carousels/form.html"
    form_class = CarouselForm
    success_url_name = "core:carousels"
    success_message = "Carousel berhasil dibuat."
    error_message = "Gagal membuat carousel."
    required_role = "administrator"


class CarouselUpdateView(BaseUpdateView):
    model = Carousel
    template_name = "core/carousels/form.html"
    form_class = CarouselForm
    success_url_name = "core:carousels"
    success_message = "Carousel berhasil diperbarui."
    error_message = "Gagal memperbarui carousel."
    required_role = "administrator"


class CarouselDeleteView(BaseDeleteView):
    model = Carousel
    success_url_name = "core:carousels"
    success_message = "Carousel berhasil dihapus."
    error_message = "Carousel tidak dapat dihapus."
    required_role = "administrator"

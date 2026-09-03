from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View
from core.forms.brand import BrandForm
from core.models.brand import Brand
from core.views.base import AccessMixin


class BrandView(AccessMixin, TemplateView):
    template_name = "core/brand.html"
    required_role = "developer"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = Brand.get_solo()
        context["brand"] = brand
        context["is_initial"] = (
            brand.name == "Brand"
            and not brand.logo
            and not brand.description
            and not brand.facebook
            and not brand.youtube
            and not brand.tiktok
            and not brand.instagram
        )
        return context


class BrandFormView(AccessMixin, View):
    template_name = "core/brand/form.html"
    required_role = "developer"

    def get(self, request):
        brand = Brand.get_solo()
        form = BrandForm(instance=brand)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        brand = Brand.get_solo()
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            messages.success(request, "Brand berhasil disimpan.")
            return redirect("core:brand")
        messages.error(request, "Gagal menyimpan brand. Periksa kembali input Anda.")
        return render(request, self.template_name, {"form": form})

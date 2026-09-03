from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import ListView, View
from core.access import has_access


class AccessMixin(LoginRequiredMixin, UserPassesTestMixin):
    required_role = "reguler"

    def test_func(self):
        return has_access(self.request.user, self.required_role)

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return super().handle_no_permission()
        raise PermissionDenied


class BaseListView(AccessMixin, ListView):
    model = None
    template_name = None
    context_object_name = None
    paginate_by = 10
    ordering = ["-created_at"]
    search_fields = []
    search_query_param = "q"
    htmx_template_name = None

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get(self.search_query_param, "").strip()
        if query and self.search_fields:
            q_objects = Q()
            for field in self.search_fields:
                q_objects |= Q(**{f"{field}__icontains": query})
            queryset = queryset.filter(q_objects)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_query"] = self.request.GET.get(self.search_query_param, "")
        return context

    def get_template_names(self):
        if self.request.htmx and self.htmx_template_name:
            return [self.htmx_template_name]
        return super().get_template_names()


class BaseCreateView(AccessMixin, View):
    template_name = None
    form_class = None
    success_url_name = None
    success_message = "Data berhasil dibuat."
    error_message = "Gagal membuat data."
    required_role = "administrator"

    def get_success_url(self):
        return reverse(self.success_url_name)

    def get_form_kwargs(self):
        return {}

    def get(self, request):
        form = self.form_class(**self.get_form_kwargs())
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST, **self.get_form_kwargs())
        if form.is_valid():
            self.save_form(form)
            messages.success(request, self.success_message)
            return redirect(self.get_success_url())
        messages.error(request, self.error_message)
        return render(request, self.template_name, {"form": form})

    def save_form(self, form):
        return form.save()


class BaseUpdateView(AccessMixin, View):
    model = None
    template_name = None
    form_class = None
    success_url_name = None
    success_message = "Data berhasil diperbarui."
    error_message = "Gagal memperbarui data."
    context_object_name = None
    required_role = "administrator"

    def get_success_url(self):
        return reverse(self.success_url_name)

    def get_form_kwargs(self):
        return {}

    def get_context_data(self, form, obj=None):
        context = {"form": form, "object": obj}
        if self.context_object_name:
            context[self.context_object_name] = obj
        return context

    def get(self, request, pk):
        obj = get_object_or_404(self.model, pk=pk)
        form = self.form_class(instance=obj, **self.get_form_kwargs())
        context = self.get_context_data(form, obj)
        return render(request, self.template_name, context)

    def post(self, request, pk):
        obj = get_object_or_404(self.model, pk=pk)
        form = self.form_class(request.POST, instance=obj, **self.get_form_kwargs())
        if form.is_valid():
            self.object = self.save_form(form)
            messages.success(request, self.success_message)
            return redirect(self.get_success_url())
        messages.error(request, self.error_message)
        context = self.get_context_data(form, obj)
        return render(request, self.template_name, context)

    def save_form(self, form):
        return form.save()


class BaseDeleteView(AccessMixin, View):
    model = None
    success_url_name = None
    success_message = "Data berhasil dihapus."
    error_message = "Data tidak dapat dihapus."
    http_method_names = ["post"]
    required_role = "administrator"

    def get_success_url(self):
        return reverse(self.success_url_name)

    def can_delete(self, request, obj):
        return True

    def post(self, request, pk):
        obj = get_object_or_404(self.model, pk=pk)
        if not self.can_delete(request, obj):
            messages.error(request, self.error_message)
            return redirect(self.get_success_url())
        try:
            obj.delete()
            messages.success(request, self.success_message)
        except Exception:
            messages.error(request, self.error_message)
        return redirect(self.get_success_url())


class BaseStatusUpdateView(AccessMixin, View):
    model = None
    status_field = "status"
    allowed_values = ("draft", "published")
    success_url_name = None
    success_message = "Status berhasil diperbarui."
    error_message = "Status tidak valid."
    http_method_names = ["post"]
    required_role = "administrator"

    def get_success_url(self):
        return reverse(self.success_url_name)

    def can_update_status(self, request, obj):
        return True

    def post(self, request, pk):
        obj = get_object_or_404(self.model, pk=pk)
        if not self.can_update_status(request, obj):
            messages.error(request, "Anda tidak memiliki izin.")
            return redirect(self.get_success_url())
        status = request.POST.get(self.status_field)
        if status in self.allowed_values:
            setattr(obj, self.status_field, status)
            obj.save()
            messages.success(request, self.success_message)
        else:
            messages.error(request, self.error_message)
        return redirect(self.get_success_url())

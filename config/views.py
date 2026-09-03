from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST


class CustomLoginView(LoginView):
    template_name = "index.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy("core:index")

    def form_valid(self, form):
        messages.success(self.request, "Login berhasil.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Username atau password salah.")
        return super().form_invalid(form)


@require_POST
def logout_view(request):
    logout(request)
    messages.info(request, "Anda telah logout.")
    return redirect("LOGOUT_REDIRECT_URL")

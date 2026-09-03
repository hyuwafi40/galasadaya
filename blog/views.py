from django.contrib import messages
from django.db.models import Q, Count
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin
from django.views.generic import TemplateView
from blog.models.article import Article
from blog.models.asset import Category, Tag
from blog.models.page import Page
from blog.models.carousel import Carousel
from blog.models.advertisement import Advertisement
from blog.models.contact import ContactMessage
from blog.models.gallery import Album
from blog.forms import ContactForm, CommentForm
import time


class AdvertisementContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ads = Advertisement.active_ads()
        ads_by_type = {}
        for ad in ads:
            ads_by_type.setdefault(ad.advertisement_type, []).append(ad)
        context["advertisements"] = ads
        context["advertisements_by_type"] = ads_by_type
        return context


class ArticleListView(AdvertisementContextMixin, ListView):
    model = Article
    template_name = "blog/index.html"
    context_object_name = "articles"
    paginate_by = 6

    def get_queryset(self):
        return Article.published.all().order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["carousels"] = Carousel.objects.all().order_by("ordering")
        context["tags"] = Tag.objects.filter(articles__status="published").distinct()[
            :10
        ]
        return context


class ArticleListPageView(AdvertisementContextMixin, ListView):
    model = Article
    template_name = "blog/article_list.html"
    context_object_name = "articles"
    paginate_by = 6

    def get_queryset(self):
        return Article.published.all().order_by("-created_at")


class ArticleDetailView(AdvertisementContextMixin, FormMixin, DetailView):
    model = Article
    template_name = "blog/article.html"
    context_object_name = "article"
    form_class = CommentForm

    def get_queryset(self):
        return Article.published.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.all().order_by("-created_at")
        context["related_articles"] = Article.published.exclude(
            pk=self.object.pk
        ).order_by("-created_at")[:3]
        context["form"] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if request.POST.get("website"):
            messages.warning(request, "Spam terdeteksi.")
            return redirect(reverse("blog:article", kwargs={"slug": self.object.slug}))

        last_comment_time = request.session.get("last_comment_time")
        if last_comment_time and (time.time() - last_comment_time) < 60:
            messages.warning(
                request, "Terlalu cepat mengirim komentar. Coba lagi nanti."
            )
            return redirect(reverse("blog:article", kwargs={"slug": self.object.slug}))

        form = self.get_form()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = self.object
            comment.save()
            request.session["last_comment_time"] = time.time()
            messages.success(request, "Komentar berhasil dikirim.")
            return redirect(reverse("blog:article", kwargs={"slug": self.object.slug}))
        return self.form_invalid(form)


class CategoryArticleListView(AdvertisementContextMixin, ListView):
    template_name = "blog/category.html"
    context_object_name = "articles"
    paginate_by = 6

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs.get("slug"))
        return Article.published.filter(category=self.category).order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        return context


class TagArticleListView(AdvertisementContextMixin, ListView):
    template_name = "blog/tag.html"
    context_object_name = "articles"
    paginate_by = 6

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug=self.kwargs.get("slug"))
        return Article.published.filter(tags=self.tag).order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.tag
        return context


class SearchView(AdvertisementContextMixin, ListView):
    template_name = "blog/search.html"
    context_object_name = "articles"
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get("q", "").strip()
        if query:
            return Article.published.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            ).order_by("-created_at")
        return Article.published.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "")
        return context


class PageListView(AdvertisementContextMixin, ListView):
    model = Page
    template_name = "blog/page_list.html"
    context_object_name = "pages"
    paginate_by = 9

    def get_queryset(self):
        return Page.published.all().order_by("-created_at")


class PageDetailView(AdvertisementContextMixin, DetailView):
    model = Page
    template_name = "blog/page.html"
    context_object_name = "page"

    def get_queryset(self):
        return Page.published.all()


class AlbumListView(AdvertisementContextMixin, ListView):
    model = Album
    template_name = "blog/gallery_list.html"
    context_object_name = "albums"
    paginate_by = 9

    def get_queryset(self):
        return Album.published.annotate(total_photos=Count("photos")).order_by(
            "-created_at"
        )


class AlbumDetailView(AdvertisementContextMixin, DetailView):
    model = Album
    template_name = "blog/gallery.html"
    context_object_name = "album"

    def get_queryset(self):
        return Album.published.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["photos"] = self.object.photos.all().order_by("created_at")
        return context


class ContactFormView(CreateView):
    model = ContactMessage
    template_name = "blog/form.html"
    form_class = ContactForm
    success_url = reverse_lazy("blog:contact")

    def form_valid(self, form):
        last_contact_time = self.request.session.get("last_contact_time")
        if last_contact_time and (time.time() - last_contact_time) < 60:
            messages.warning(
                self.request, "Terlalu cepat mengirim pesan. Coba lagi nanti."
            )
            return redirect(self.success_url)
        self.request.session["last_contact_time"] = time.time()
        messages.success(self.request, "Pesan Anda berhasil dikirim.")
        return super().form_valid(form)


class RobotsView(TemplateView):
    template_name = "blog/robots.txt"
    content_type = "text/plain"


class SitemapView(TemplateView):
    template_name = "blog/sitemap.xml"
    content_type = "application/xml"

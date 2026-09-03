from django.contrib import admin
from blog.models.comment import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "article", "created_at")
    search_fields = ("name", "text")

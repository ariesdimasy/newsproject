from django.contrib import admin
from django.utils import timezone
# Register your models here.
from .models import Category, News


class CategoryAdmin(admin.ModelAdmin):

    list_display = ("name", "created_at")

    search_fields = ["name"]


class NewsAdmin(admin.ModelAdmin):

    list_display = ("title", "status", "user", "created_at")

    fields = ("title", "content", "excerpt", "cover", "status", "categories")

    search_fields = ["title"]

    list_filter = ("status", )

    def save_model(self, request, obj, form, change):

        if not obj.user_id:
            obj.user = request.user

            if form.cleaned_data.get("status") == 1:
                obj.published_at = None
            else:
                obj.published_at = timezone.now()


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

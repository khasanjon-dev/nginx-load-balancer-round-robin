from django.contrib import admin

from news.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

from django.contrib import admin

from sharing_is_caring.main_content.models import Post


@admin.register(Post)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('type', 'condition', 'item_type', 'name', 'user')
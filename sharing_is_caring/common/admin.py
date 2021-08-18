from django.contrib import admin

from sharing_is_caring.common.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'user_to_be_commented', 'user')
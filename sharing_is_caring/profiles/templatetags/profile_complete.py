from django import template

from sharing_is_caring.profiles.models import UserProfile

register = template.Library()

@register.inclusion_tag('shared/profile_complete_notification.html', takes_context=True)
def profile_complete_notification(context):
    profile = UserProfile(context.request.user.id)
    context['is_complete'] = profile.is_complete
    return context

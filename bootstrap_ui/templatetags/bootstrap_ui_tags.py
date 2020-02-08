from django.conf import settings
from django.template import Library

register = Library()


@register.simple_tag(takes_context=True)
def get_value_from_session_or_cookie(context, key):
    request = context['request']

    try:
        # First check for key in session
        # If no session is available this throws an AttributeError, if the key is not available in an existing session
        # this throws a KeyError
        return request.session[key]
    except (AttributeError, KeyError):
        try:
            # Second check for key in cookies
            return request.COOKIES[key]
        except KeyError:
            # Third fallback to settings or return default value
            return getattr(settings, key, '')

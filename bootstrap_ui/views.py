from django import http
from django.utils.http import is_safe_url


def set_theme(request):
    """
    Redirect to a given url while setting the chosen theme in the session or cookie. The url and the theme identifier
    need to be specified in the request parameters.

    Since this view changes how the user will see the rest of the site, it must only be accessed as a POST request. If
    called as a GET request, it will redirect to the page in the request (the 'next' parameter) without changing any
    state.
    """
    next = request.POST.get('next', request.GET.get('next'))

    if not is_safe_url(url=next, host=request.get_host()):
        next = request.META.get('HTTP_REFERER')

        if not is_safe_url(url=next, host=request.get_host()):
            next = '/'

    response = http.HttpResponseRedirect(next)

    if request.method == 'POST':
        theme = request.POST.get('theme', None)

        if theme:
            if hasattr(request, 'session'):
                request.session['DJANGO_BOOTSTRAP_UI_THEME'] = theme
            else:
                response.set_cookie('DJANGO_BOOTSTRAP_UI_THEME', theme)

    return response

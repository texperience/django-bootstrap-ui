from django.shortcuts import render_to_response
from django.template import RequestContext

def render_named_template(request, template):
    return render_to_response(template, RequestContext(request))

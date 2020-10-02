from django.shortcuts import render
from django.http import HttpResponseNotFound

from django.http import HttpResponse

from . import util
from .mdtohtml import convert


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    e = util.get_entry(title)
    if e:
        return HttpResponse(convert(e))
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')

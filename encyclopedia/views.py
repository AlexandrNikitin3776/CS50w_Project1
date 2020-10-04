from django.http import response
from django.shortcuts import render
from django.http import HttpResponseNotFound

from django.http import HttpResponse

from . import util
from .mdtohtml import convert


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, page_title):
    res = util.get_entry(page_title)
    if res:
        return render(request, "encyclopedia/entry.html",{
            "page_title": page_title,
            "content": convert(res),
        })
    else:
        return render(request, "encyclopedia/pagenotfound.html")

# from django.http import response
# from django.http import request
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import util
from .mdtohtml import convert
import random


def index(request):
    return render(
        request,
        "encyclopedia/index.html",
        {
            "entries": util.list_entries(),
        },
    )


def entry(request, page_title):
    res = util.get_entry(page_title)
    if res:
        return render(
            request,
            "encyclopedia/entry.html",
            {
                "page_title": page_title,
                "content": convert(res),
            },
        )
    else:
        return render(request, "encyclopedia/pagenotfound.html")


def randompage(request):
    pagelist = util.list_entries()
    print("html to go", reverse("entry", args=[random.choice(pagelist)]))
    return HttpResponseRedirect(reverse("entry", args=[random.choice(pagelist)]))

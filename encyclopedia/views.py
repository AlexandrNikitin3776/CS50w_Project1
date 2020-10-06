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
    random_page = random.choice(util.list_entries())
    return HttpResponseRedirect(reverse("entry", args=[random_page]))


def searchpage(request):
    if request.method == "GET":
        print(request.GET.get("search"))
        searchphraze = request.GET.get("search").lower()
        pages = util.list_entries()
        if searchphraze in list(map(lambda x: x.lower(), pages)):
            return HttpResponseRedirect(reverse("entry", args=[searchphraze]))
        searchresults = []
        for p in pages:
            if searchphraze in p.lower():
                searchresults.append(p)
        if searchresults:
            return render(request, "encyclopedia/search_page.html")
            # TODO: Add search_page template
            # TODO: Change there arn't any search results (empty search results in search template)
    return render(request, "encyclopedia/pagenotfound.html")

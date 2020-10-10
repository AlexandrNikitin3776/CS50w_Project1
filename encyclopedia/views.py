import random
from django.forms import utils
from django.http import request

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import util
from .mdtohtml import convert
from .forms import NewPageForm


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
        return render(
            request,
            "encyclopedia/pagenotfound.html",
            {
                "page_title": page_title,
            },
        )


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
        return render(
            request,
            "encyclopedia/search_page.html",
            {
                "entries": searchresults,
            },
        )


def createnewpage(request):
    if request.method == "POST":
        form = NewPageForm(request.POST or None)
        if form.is_valid():
            page_title = form.cleaned_data["page_title"]
            content = form.cleaned_data["content"]
            util.save_entry(page_title, content)
            return HttpResponseRedirect(reverse("entry", args=[page_title]))
        else:
            return render(
                request,
                "encyclopedia/new_page.html",
                {
                    "form": form,
                },
            )

    return render(
        request,
        "encyclopedia/new_page.html",
        {
            "form": NewPageForm(),
        },
    )

from encyclopedia.views import createnewpage
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/random_page", views.randompage, name="random_page"),
    path("wiki/search_page", views.searchpage, name="search_page"),
    path("wiki/new_page", views.createnewpage, name="new_page"),
    path("wiki/<str:page_title>/edit", views.editpage, name="edit_page"),
    path("wiki/<str:page_title>", views.entry, name="entry"),
]

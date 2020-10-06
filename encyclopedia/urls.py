from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/random_page", views.randompage, name="random_page"),
    path("wiki/search_page", views.searchpage, name="search_page"),
    path("wiki/<str:page_title>", views.entry, name="entry"),
]

from django.urls import URLPattern, path

from .views import GetCardView, MainView

urlpatterns: list[URLPattern] = [
    path("", MainView.as_view(), name="main"),
    path("get_card/", GetCardView.as_view(), name="get_card"),
]

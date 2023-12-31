from django.urls import path

from .views import GamePage, IndexView, ListCounties, ResultsCountries

urlpatterns = [
    path("list_of_countries", ListCounties.as_view(), name="list_of_countries"),
    path("game/", GamePage.as_view(), name="game"),
    path("game/<path:continent_name>", GamePage.as_view(), name="game"),
    path("results", ResultsCountries.as_view(), name="results"),
    path("", IndexView.as_view(), name="index"),
]

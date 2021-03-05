from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="GFarmingHome"),
    path("transport/", views.transport, name="Transport"),
    path("carservice/", views.carservice, name="Cars"),
    path("tractorservice/", views.tractorservice, name="TractorService"),
    path("search/", views.search, name="Search"),
    path("signup/", views.siup, name="Siup"),
    path("login/", views.lon, name="Lon"),
    path("empindex/", views.empindex, name="Empindex"),
    path("empuserwork/", views.empuserwork, name="Empuserwork"),
    path("invoice/", views.invoice, name="Invoice")
]
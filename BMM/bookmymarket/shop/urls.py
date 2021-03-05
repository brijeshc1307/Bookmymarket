from . import views
from django.urls import path
from .middlewares.auth import auth_middleware
urlpatterns = [

    path("", views.index, name="ShopHome"),
    path("gardenning/", views.gardenning, name="Gardenning"),
    path("fertilizers/", views.fertilizers, name="Fertilizers"),
    path("pesticides/", views.pesticides, name="Pesticides"),
    path("seed/", views.seed, name="Seed"),
    path("agriMachinery/", views.agriMachinery, name="AgriMachinary"),
    path("search/", views.search, name="Search"),
    path("aboutus/", views.aboutus, name="AboutUs"),
    path("contactus/", views.contactus, name="ContactUs"),
    path("services/", views.services, name="Services"),
    path("carrier/", views.carrier, name="Carrier"),
    path("addcart/", views.addcart, name="AddCart"),
    path("buynow/", views.buynow, name="BuyNow"),
    path("checkout/", auth_middleware(views.checkout), name="Checkout"),
    path("cheout/", views.cheout, name="Cheout"),
    path("signup/", views.signup, name="Signup"),
    path("login/", views.login, name="Login"),
    path("logout/", views.logout, name="Logout"),
    path("privacypolicy/", views.privacypolicy, name="Privacypolicy"),
    path("returnpolicy/", views.returnpolicy, name="Returnpolicy"),
    path("productdetail/", views.productdetail, name="Productdetail"),
    path("invoice/", views.invoice, name="Invoice"),
    path("customerdassboard/", auth_middleware(views.customerdassboard), name="Customerdassboard"),

    path("continueshopping/", views.continueshopping, name="ContinueShopping")

]
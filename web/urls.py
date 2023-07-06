from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
# from .views import ProductDetailView
from django.views.generic.base import TemplateView

# handler404 = '.webviews.custom_404_view'

urlpatterns = [
    path('', views.index, name="index"),
    path('contacto/', views.contacto, name="contacto"),
    path('nosotros/', views.nosotros, name="nosotros"),
    # path('tienda/', views.tienda, name="tienda"),
    # path('tienda/<slug:producturl>/', ProductDetailView.as_view(), name='product_detail'),
    path('servicios/', views.servicios, name="servicios"),
    path('pauta/', views.pauta, name="pauta"),
    path('cookies/', views.cookies, name="cookies"),
    path('privacy/', views.privacy, name="privacy"),
    path("robots.txt", views.robots, name="robots"),
]
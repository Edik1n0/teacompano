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
    path('servicios/formulario-solicitud/', views.form, name="formulario"),
    path('pauta/', views.pauta, name="pauta"),
    path('politica-cookies/', views.cookies, name="cookies"),
    path('politica-privacidad/', views.privacy, name="privacy"),
    path("robots.txt", views.robots, name="robots"),
]
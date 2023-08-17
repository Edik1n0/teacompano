from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .views import ServiceDetailView
from django.views.generic.base import TemplateView

# handler404 = '.webviews.custom_404_view'

urlpatterns = [
    path('', views.index, name="index"),
    path('contacto/', views.contacto, name="contacto"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('servicios/', views.servicios, name="servicios"),
    path('servicios/<slug:serviceurl>/', ServiceDetailView.as_view(), name='service_detail'),
    path('servicios/formulario-solicitud/', views.form, name="formulario"),
    path('pauta/', views.pauta, name="pauta"),
    path('politica-cookies/', views.cookies, name="cookies"),
    path('politica-privacidad/', views.privacy, name="privacy"),
    path("robots.txt", views.robots, name="robots"),
    path('generate_pdf/<int:kardex_id>/', views.generate_pdf, name='generate_pdf'),
]
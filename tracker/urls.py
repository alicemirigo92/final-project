from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage_html, name='homepage_html'),
    path('api/', views.homepage_api, name='homepage_api'),
    path('add-activity/', views.add_activity, name='add_activity'),
    path('add-badge/', views.add_badge, name='add_badge'),
    path('calculate-emissions/', views.calculate_emissions, name='calculate_emissions'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('add-activity/', views.add_activity, name='add_activity'),
    path('add-badge/', views.add_badge, name='add_badge'),
    path('insights/', views.insights, name='insights'),
]

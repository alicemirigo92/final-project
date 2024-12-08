from django.contrib import admin
from django.urls import path
from tracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage_html, name='homepage'),  # Homepage
    path('add-activity/', views.add_activity, name='add_activity'),  # Add activity
    path('add-badge/', views.add_badge, name='add_badge'),  # Add badge
    path('insights/', views.insights, name='insights'),  # View insights
]

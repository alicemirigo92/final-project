from django.contrib import admin
from django.urls import path, include
from tracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage_html, name='homepage'),  # Change to `homepage_html` for HTML output
    path('api/', include('tracker.urls')),  # For tracker API views
]

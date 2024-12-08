from django.contrib import admin
from .models import Activity, Badge

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type', 'value', 'date')  # Corrected fields
    search_fields = ('activity_type', 'user__username')  # Allow searching by user and activity type

class BadgeAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'earned_at')  # Corrected fields
    search_fields = ('name', 'user__username')  # Allow searching by user and badge name

admin.site.register(Activity, ActivityAdmin)
admin.site.register(Badge, BadgeAdmin)

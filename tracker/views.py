from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Activity, Badge
from .forms import ActivityForm, BadgeForm


# View for displaying the homepage in HTML
def homepage_html(request):
    activities = Activity.objects.all()
    badges = Badge.objects.all()
    context = {
        'activities': activities,
        'badges': badges,
    }
    return render(request, 'tracker/homepage.html', context)


# API endpoint for homepage (JSON response)
def homepage_api(request):
    activities = list(Activity.objects.values())
    badges = list(Badge.objects.values())
    response_data = {
        'activities': activities,
        'badges': badges,
    }
    return JsonResponse(response_data)


# View to add a new activity
def add_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage_html')
    else:
        form = ActivityForm()
    return render(request, 'tracker/add_activity.html', {'form': form})


# View to add a new badge
def add_badge(request):
    if request.method == 'POST':
        form = BadgeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage_html')
    else:
        form = BadgeForm()
    return render(request, 'tracker/add_badge.html', {'form': form})


# View to calculate emissions (API integration)
def calculate_emissions(request):
    if request.method == 'POST':
        activity_type = request.POST.get('activity_type')
        value = request.POST.get('value')
        unit = request.POST.get('unit')
        # Replace with actual API call logic
        api_result = {
            "activity_type": activity_type,
            "value": value,
            "unit": unit,
            "estimated_emission": "Mocked Data",
        }
        return JsonResponse(api_result)
    return render(request, 'tracker/calculate_emissions.html')

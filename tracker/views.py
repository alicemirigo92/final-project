from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Activity, Badge
from .forms import ActivityForm, BadgeForm

@login_required
def homepage_html(request):
    """
    Render the homepage with activities and badges for the logged-in user.
    """
    activities = Activity.objects.filter(user=request.user)
    badges = Badge.objects.filter(user=request.user)
    context = {
        'activities': activities,
        'badges': badges,
    }
    return render(request, 'tracker/homepage.html', context)

def check_for_badges(user):
    """
    Check if the user qualifies for new badges based on activities.
    """
    # Example badge: "First Step"
    if not Badge.objects.filter(user=user, name="First Step").exists():
        if Activity.objects.filter(user=user).exists():
            Badge.objects.create(
                user=user,
                name="First Step",
                description="Congratulations! You've logged your first activity."
            )

    # Example badge: "Water Saver"
    if Activity.objects.filter(user=user, activity_type="water").count() >= 5:
        if not Badge.objects.filter(user=user, name="Water Saver").exists():
            Badge.objects.create(
                user=user,
                name="Water Saver",
                description="Great! You've logged activities related to water usage."
            )

@login_required
def add_activity(request):
    """
    Allow the user to add a new activity.
    """
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.user = request.user
            activity.save()
            check_for_badges(request.user)  # Check for badges
            return redirect('homepage')
    else:
        form = ActivityForm()
    return render(request, 'tracker/add_activity.html', {'form': form})

@login_required
def add_badge(request):
    """
    Allow admins to manually add a badge for a user.
    """
    if request.method == 'POST':
        form = BadgeForm(request.POST)
        if form.is_valid():
            badge = form.save(commit=False)
            badge.user = request.user
            badge.save()
            return redirect('homepage')
    else:
        form = BadgeForm()
    return render(request, 'tracker/add_badge.html', {'form': form})

@login_required
def insights(request):
    """
    Show insights about the user's activities and badges.
    """
    activities = Activity.objects.filter(user=request.user)
    badges = Badge.objects.filter(user=request.user)
    return render(request, 'tracker/insights.html', {
        'activities': activities,
        'badges': badges,
    })

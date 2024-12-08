from django.test import TestCase
from django.contrib.auth.models import User
from .models import Activity, Badge

class TrackerTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.activity = Activity.objects.create(user=self.user, activity_type='transportation', value=10)

    def test_activity_creation(self):
        self.assertEqual(self.activity.value, 10)

    def test_badge_assignment(self):
        badge = Badge.objects.create(user=self.user, name='First Step', description='First activity logged')
        self.assertEqual(badge.name, 'First Step')

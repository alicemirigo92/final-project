from django.db import models
from django.contrib.auth.models import User


class Activity(models.Model):
    ACTIVITY_CHOICES = [
        ('energy', 'Energy'),
        ('water', 'Water'),
        ('transportation', 'Transportation'),
        ('waste', 'Waste'),
    ]
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_CHOICES)
    value = models.FloatField()
    unit = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.activity_type} - {self.value} {self.unit}"


class Badge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    earned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# pricing/models.py

from django.db import models
from django.contrib.auth.models import User

DAYS_OF_WEEK = [
    ('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'),
    ('Thu', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday'), ('Sun', 'Sunday')
]

class PricingConfig(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    valid_days = models.JSONField()  
    base_distance_km = models.FloatField()
    base_price = models.FloatField()
    additional_price_per_km = models.FloatField()
    waiting_charge_per_minute = models.FloatField()
    free_wait_time_minutes = models.IntegerField(default=3)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({'Active' if self.active else 'Inactive'})"


class TimeMultiplier(models.Model):
    pricing_config = models.ForeignKey(PricingConfig, on_delete=models.CASCADE, related_name='time_multipliers')
    lower_bound = models.FloatField()  
    upper_bound = models.FloatField()  
    multiplier = models.FloatField()

    def __str__(self):
        return f"{self.lower_bound}–{self.upper_bound} mins: {self.multiplier}x"


class PricingLog(models.Model):
    pricing_config = models.ForeignKey(PricingConfig, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)  # e.g., "created", "updated", "deleted"
    actor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.action} by {self.actor} on {self.timestamp}"

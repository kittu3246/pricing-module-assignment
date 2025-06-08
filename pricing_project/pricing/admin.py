from django.contrib import admin
from .models import PricingConfig, TimeMultiplier, PricingLog
from .signals import set_actor

class TimeMultiplierInline(admin.TabularInline):
    model = TimeMultiplier
    extra = 1

@admin.register(PricingConfig)
class PricingConfigAdmin(admin.ModelAdmin):
    inlines = [TimeMultiplierInline]

    def save_model(self, request, obj, form, change):
        set_actor(request.user)
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        set_actor(request.user)
        super().delete_model(request, obj)

@admin.register(PricingLog)
class PricingLogAdmin(admin.ModelAdmin):
    list_display = ('pricing_config', 'action', 'actor', 'timestamp', 'description')
    readonly_fields = ('pricing_config', 'action', 'actor', 'timestamp', 'description')
    list_filter = ('action', 'actor', 'timestamp')
    search_fields = ('description', 'actor__username')

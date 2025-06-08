from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PricingConfig
from datetime import datetime
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("<h1>Welcome to Pricing Module</h1>")

class CalculatePriceView(APIView):
    def post(self, request):
        try:
            data = request.data
            distance = float(data['distance'])  # in km
            duration = float(data['duration'])  # in minutes
            waiting_time = float(data['waiting_time'])  # in minutes
            today_str = datetime.today().strftime('%a')  # e.g., 'Mon', 'Tue', etc.

            # Get the active pricing config for today
            configs = PricingConfig.objects.filter(active=True)
            matching_config = None
            for config in configs:
                if today_str in config.valid_days:
                    matching_config = config
                    break

            if not matching_config:
                return Response({"error": "No pricing config active today."}, status=404)

            # Base price and additional distance
            base_price = matching_config.base_price
            base_distance = matching_config.base_distance_km
            additional_distance = max(0, distance - base_distance)
            additional_price = additional_distance * matching_config.additional_price_per_km

            # Time multiplier
            multiplier = 1.0
            time_multipliers = matching_config.time_multipliers.all()

            for tm in time_multipliers:
                if tm.lower_bound <= duration < tm.upper_bound:
                    multiplier = tm.multiplier
                    break

            # Waiting charge
            free_wait = matching_config.free_wait_time_minutes
            extra_wait = max(0, waiting_time - free_wait)
            wait_charge = extra_wait * matching_config.waiting_charge_per_minute

            # Total price calculation
            total_price = (base_price + additional_price) * multiplier + wait_charge
            total_price = round(total_price, 2)

            return Response({"total_price": total_price})

        except Exception as e:
            return Response({"error": f"Internal server error: {str(e)}"}, status=500)

from django.http import JsonResponse
import logging
import requests

logger = logging.getLogger(__name__)

def track_user(request):
    # Simulated user consent check
    consent = request.GET.get('consent', 'no')  # Ensure you show a consent page first
    if consent.lower() != 'yes':
        return JsonResponse({"error": "User consent required"}, status=403)

    # Capture IP, user agent, and geolocation data
    ip = get_client_ip(request)
    user_agent = request.META.get('HTTP_USER_AGENT', 'Unknown')

    # Use a geolocation API to find location (e.g., ip-api.com)
    location_data = get_location_from_ip(ip)

    # Log details
    logger.info(f"IP: {ip}, User Agent: {user_agent}, Location: {location_data}")

    return JsonResponse({
        "message": "Data captured for educational purposes",
        "IP": ip,
        "User Agent": user_agent,
        "Location": location_data
    })

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_location_from_ip(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        return response.json() if response.status_code == 200 else {}
    except Exception as e:
        return {"error": "Could not retrieve location"}

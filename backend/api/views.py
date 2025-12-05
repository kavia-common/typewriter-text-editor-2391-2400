# Minimal health endpoint only, now handled in texts app as well.
from django.http import JsonResponse

# PUBLIC_INTERFACE
def health(request):
    """Health check endpoint that returns {status: 'ok'}."""
    return JsonResponse({"status": "ok"})

import os
import json
import uuid
from django.conf import settings
from django.http import JsonResponse, HttpResponseNotAllowed, Http404
from django.views.decorators.csrf import csrf_exempt
from .serializers import validate_text_payload, ValidationError

TEXTS_DIR = os.path.join(settings.BASE_DIR, "texts_storage")

if not os.path.exists(TEXTS_DIR):
    os.makedirs(TEXTS_DIR, exist_ok=True)

def text_file_path(text_id):
    return os.path.join(TEXTS_DIR, f"{text_id}.json")

# PUBLIC_INTERFACE
def health_view(request):
    """GET /api/health/"""
    return JsonResponse({"status": "ok"})

@csrf_exempt
def texts_collection(request):
    """
    /api/texts/
    POST: Save a text blob and metadata.
    GET: List all saved text entries.
    """
    if request.method == "POST":
        try:
            payload = json.loads(request.body)
            data = validate_text_payload(payload)
        except (json.JSONDecodeError, UnicodeDecodeError):
            return JsonResponse({"error": "Invalid JSON."}, status=400)
        except ValidationError as e:
            return JsonResponse({"error": str(e)}, status=400)

        text_id = str(uuid.uuid4())
        data.update({"id": text_id})
        file_path = text_file_path(text_id)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f)
        return JsonResponse(data, status=201)

    elif request.method == "GET":
        entries = []
        for fname in os.listdir(TEXTS_DIR):
            if fname.endswith(".json"):
                try:
                    with open(os.path.join(TEXTS_DIR, fname), "r", encoding="utf-8") as f:
                        data = json.load(f)
                        summary = {
                            "id": data.get("id"),
                            "title": data.get("title"),
                            "updated_at": data.get("updated_at"),
                        }
                        entries.append(summary)
                except Exception:
                    continue
        entries.sort(key=lambda e: e.get("updated_at") or "", reverse=True)
        return JsonResponse(entries, safe=False)
    else:
        return HttpResponseNotAllowed(["GET", "POST"])

@csrf_exempt
def texts_detail(request, text_id):
    """
    /api/texts/{id}/
    GET: Fetch single entry.
    DELETE: Remove entry.
    """
    file_path = text_file_path(text_id)
    if not os.path.exists(file_path):
        raise Http404("Text entry not found.")

    if request.method == "GET":
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return JsonResponse(data)

    elif request.method == "DELETE":
        os.remove(file_path)
        return JsonResponse({"deleted": text_id})

    else:
        return HttpResponseNotAllowed(["GET", "DELETE"])

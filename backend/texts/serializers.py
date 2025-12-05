from datetime import datetime

class ValidationError(Exception):
    """Mimics DRF's ValidationError for simple schema validation."""
    pass

# PUBLIC_INTERFACE
def validate_text_payload(data):
    """Validate text persistence payload: must include title and text as str."""
    if not isinstance(data, dict):
        raise ValidationError("Payload must be a JSON object.")
    title = data.get("title")
    text = data.get("text")
    if not isinstance(title, str) or not title.strip():
        raise ValidationError("Title must be a non-empty string.")
    if not isinstance(text, str):
        raise ValidationError("Text must be a string.")
    # Optionally parse updated_at or set it
    return {
        "title": title.strip(),
        "text": text,
        "updated_at": data.get("updated_at") or datetime.utcnow().isoformat(),
    }

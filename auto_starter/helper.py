import json
import re

def repair_json(json_str: str) -> str:
    """Repair JSON string by removing code fences, handling triple quotes.
    Returns a cleaned raw JSON string.
    """
    json_str = json_str.strip()
    # Remove opening ```json or ```
    json_str = re.sub(r'```(json)?\s*', '', json_str)  # Opening
    json_str = re.sub(r'\s*```', '', json_str)        # Closing
    json_str = json_str.strip()  # Extra trim

    # Replace triple quotes with double quotes
    json_str = re.sub(r'"""(.*?)"""', r'"\1"', json_str, flags=re.DOTALL)

    # Validate but don’t return dict
    try:
        json.loads(json_str)
    except Exception as e:
        raise ValueError(f"Invalid JSON: {e}")

    # Return the cleaned raw JSON string
    return json_str
import json
import re

def repair_json(json_str: str) -> str:
    """Improved JSON fixer: Remove code fences fully, handle triple quotes, add missing commas."""
    json_str = json_str.strip()
    # Remove opening ```json
    json_str = re.sub(r'```(json)?\s*', '', json_str)  # Opening
    json_str = re.sub(r'\s*```', '', json_str)  # Closing
    json_str = json_str.strip()  # Extra trim
    # Replace triple quotes with double (for multi-line)
    json_str = re.sub(r'"""(.*?)"""', r'"\1"', json_str, flags=re.DOTALL)
    # No aggressive escaping - rely on LLM
    # Add missing comma/brace heuristic
    try:
        json.loads(json_str)  # Test
        return json_str
    except:
        # Fix last key without comma
        json_str = re.sub(r'([^\s"]+)\s*:\s*([^\s{["]+?)\s*(\n\s*[\]}])', r'\1: "\2"\3', json_str)  # Wrap unquoted values
        json_str = re.sub(r'(\w+)"\s*(\n\s*})', r'\1",\2', json_str)  # Missing comma
        return json_str
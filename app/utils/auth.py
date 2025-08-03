import json
import os

KEYS_FILE = os.path.join(os.path.dirname(__file__), '../../data/keys.json')

def is_valid_key(key: str) -> bool:
    try:
        with open(KEYS_FILE, 'r') as f:
            keys = json.load(f)
        return key in keys.get("valid_keys", [])
    except Exception:
        return False

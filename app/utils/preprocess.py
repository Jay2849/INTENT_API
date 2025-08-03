import re

def clean_text(text: str) -> str:
    # Example cleaning steps: lowercasing, removing special chars, etc.
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    text = text.strip()
    return text

import re
import joblib
import os
import pandas as pd
from app.utils.preprocess import clean_text

# Load your model once
MODEL_PATH = os.path.join(os.path.dirname(__file__), '../data/models/classifier.pkl')
model = joblib.load(MODEL_PATH)

# Define some rule-based keywords for quick filtering (example)
KEYWORD_INTENTS = {
    "php": "PHPLead",
    "seo": "SEOLead",
    "vendor": "VendorLead",
    "oil": "OilLead"
}

def get_intent(text: str) -> str:
    # 1. Rule-based keyword matching
    lowered = text.lower()
    for keyword, intent in KEYWORD_INTENTS.items():
        if re.search(r'\b' + re.escape(keyword) + r'\b', lowered):
            return intent

    # 2. ML model prediction
    cleaned = clean_text(text)
    pred = model.predict([cleaned])
    return pred[0]

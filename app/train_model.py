import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load and filter dataset
df = pd.read_csv("data/raw/SEOLeadDataset.csv")
df = df[df['intent'].isin(['SEOLead', 'NoLead', 'NotLead'])]

X = df['Text']
y = df['intent']

# Build pipeline
pipeline = make_pipeline(
    TfidfVectorizer(lowercase=True, stop_words='english'),
    LogisticRegression(max_iter=1000)
)

# Train/test split and fit
X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
pipeline.fit(X_train, y_train)

# Save model
joblib.dump(pipeline, "data/models/classifier.py")
print("✅ Model trained and saved.")

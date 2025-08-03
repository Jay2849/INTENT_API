# 🧠 Intent Classification API

A FastAPI-based project that uses both rule-based logic and machine learning to classify textual input into intent categories (e.g., `SEOLead`, `NoLead`, `NotLead`, etc.). Useful for lead qualification, support routing, and text analysis tasks.

---

## 🚀 Features

- 🔐 **API Key Authentication**
- 🤖 **Hybrid Intent Detection**: Combines rule-based keyword matching and ML classification
- 🧼 **Text Preprocessing**: Cleans input text before prediction
- 📦 **Model Training**: Includes script to train and save your own model
- 🧪 **Testable REST API**: Simple endpoint for predictions

## 🧪 API Usage

### 📬 Endpoint: `/predict-intent`

**Method:** `POST`  
**Request Body:**

```json
{
  "key": "your-api-key",
  "text": "Looking for SEO services for my company",
  "guid": "123-abc"
}

Response:

{
  "intent": "SEOLead",
  "text": "Looking for SEO services for my company",
  "guid": "123-abc"
}


### **🛠️ Setup Instructions**
1. Clone the Repository
git clone https://github.com/Jay2849/INTENT_API.git
cd INTENT_API

2. Install Requirements
pip install -r requirements.txt

3. Train the Model
python train_model.py

4.Run the API
uvicorn main:app --reload


### **🔑 API Key Setup**
Create a file at data/keys.json:
{
  "valid_keys": ["your-api-key"]
}
Use this key when sending requests to the API.


### **🧹 Text Preprocessing**
The system applies basic text cleaning before prediction:
-Converts to lowercase
-Removes special characters
-Strips extra whitespace

Example:
clean_text("Buy SEO services!!!")  # Output: "buy seo services"


### **🧠 Model Details**
-> Vectorizer: TfidfVectorizer with English stopwords
-> Classifier: LogisticRegression
-> Training: Uses filtered labeled dataset (SEOLead, NoLead, NotLead)

### **📄 License**
This project is open-source and free to use under the MIT License.
Let me know if you'd like this as a downloadable `.md` file or if you want to add badges, contributors, or deployment instructions (e.g. Render, Heroku, Docker).

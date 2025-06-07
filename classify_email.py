import sys
import joblib

def load_model_and_vectorizer(model_path='svm_spam_classifier.pkl', vectorizer_path='tfidf_vectorizer.pkl'):
    try:
        model = joblib.load(model_path)
        vectorizer = joblib.load(vectorizer_path)
        return model, vectorizer
    except Exception as e:
        print("Error loading model/vectorizer:", e)
        sys.exit(1)

def predict_email(text, model, vectorizer):
    vect_text = vectorizer.transform([text])
    prediction = model.predict(vect_text)
    return "Spam" if prediction[0] == 1 else "Ham"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python classify_email.py \"Your email content here\"")
        sys.exit(1)

    email_text = sys.argv[1]
    model, vectorizer = load_model_and_vectorizer()
    result = predict_email(email_text, model, vectorizer)
    print(f"Prediction: {result}")

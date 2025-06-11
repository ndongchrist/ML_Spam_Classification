from flask import Flask, render_template, request
import joblib

# Load model and vectorizer
model = joblib.load("svm_spam_classifier.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    message = ""
    if request.method == "POST":
        message = request.form["email"]
        vector = vectorizer.transform([message])
        pred = model.predict(vector)[0]
        prediction = "Spam" if pred == 1 else "Ham"
    return render_template("index.html", prediction=prediction, message=message)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

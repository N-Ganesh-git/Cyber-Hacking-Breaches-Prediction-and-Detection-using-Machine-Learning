from flask import Flask, render_template, request
import os
import pickle

from feature import FeatureExtraction

app = Flask(__name__)

# -----------------------------
# Load model once at startup
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


@app.route("/", methods=["GET", "POST"])
def index():
    prediction_text = None
    url_value = ""
    phishing_percent = -1  # this will be used in UI if needed

    if request.method == "POST":
        url_value = request.form.get("url", "").strip()

        if not url_value:
            prediction_text = "Please enter a URL."
        else:
            # 1. Extract features
            extractor = FeatureExtraction(url_value)
            features = extractor.get_features_array()

            # 2. Predict label and probability
            pred = model.predict(features)[0]

            # Handle probability of phishing safely
            phishing_prob = None
            try:
                proba = model.predict_proba(features)[0]
                classes = list(model.classes_)

                # we assume label "1" means phishing
                if 1 in classes:
                    phishing_index = classes.index(1)
                    phishing_prob = proba[phishing_index]
                else:
                    # fallback: take probability of "positive" class
                    phishing_prob = proba.max()
            except Exception:
                phishing_prob = None

            if pred == 1:
                # Phishing
                if phishing_prob is not None:
                    phishing_percent = round(phishing_prob * 100, 2)
                    prediction_text = f"⚠️ This URL is likely PHISHING ({phishing_percent}% confidence)."
                else:
                    prediction_text = "⚠️ This URL is likely PHISHING."
            else:
                # Legitimate
                if phishing_prob is not None:
                    legit_percent = round((1 - phishing_prob) * 100, 2)
                    prediction_text = f"✅ This URL appears LEGITIMATE ({legit_percent}% confidence)."
                    phishing_percent = round(phishing_prob * 100, 2)
                else:
                    prediction_text = "✅ This URL appears LEGITIMATE."

    return render_template(
        "index.html",
        url=url_value,
        prediction_text=prediction_text,
        xx=phishing_percent,  # you can use this in HTML for extra display
    )


if __name__ == "__main__":
    app.run(debug=True)

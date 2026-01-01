from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import pickle
import os
import json
import uuid

app = Flask(__name__)
CORS(app)   # ✅ THIS FIXES FRONTEND ERROR

# ---------------- PATH SETUP ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "models")

# ---------------- LOAD MODELS ----------------
crop_model = load_model(os.path.join(MODEL_DIR, "crop_model.h5"))
diabetes_model = pickle.load(open(os.path.join(MODEL_DIR, "diabetes_model.pkl"), "rb"))

# Load class labels for crop model
with open(os.path.join(MODEL_DIR, "class_indices.json")) as f:
    class_indices = json.load(f)

# Reverse mapping: index -> class name
index_to_class = {v: k for k, v in class_indices.items()}

# ---------------- ROUTES ----------------
@app.route("/")
def home():
    return "Smart Disease Assistance System Running"

# ----------- CROP DISEASE PREDICTION ----------
@app.route("/predict-crop", methods=["POST"])
def predict_crop():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]

    temp_filename = f"{uuid.uuid4().hex}.jpg"
    temp_path = os.path.join(BASE_DIR, temp_filename)
    file.save(temp_path)

    try:
        img = image.load_img(temp_path, target_size=(224, 224))
        img = image.img_to_array(img) / 255.0
        img = np.expand_dims(img, axis=0)

        pred = crop_model.predict(img)
        confidence = float(np.max(pred))
        class_index = int(np.argmax(pred))
        disease_name = index_to_class[class_index]

        return jsonify({
            "disease": disease_name,
            "confidence": round(confidence * 100, 2)
        })
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

# ----------- MEDICAL RISK PREDICTION ----------
@app.route("/medical-chat", methods=["POST"])
def medical_chat():
    data = request.json

    feature_order = [
        "Pregnancies",
        "Glucose",
        "BloodPressure",
        "SkinThickness",
        "Insulin",
        "BMI",
        "DiabetesPedigreeFunction",
        "Age"
    ]

    try:
        features = [data[f] for f in feature_order]
    except KeyError as e:
        return jsonify({"error": f"Missing field: {str(e)}"}), 400

    prob = diabetes_model.predict_proba([features])[0][1]

    return jsonify({
        "risk": "High" if prob > 0.6 else "Low",
        "probability": round(prob * 100, 2),
        "note": "This is a risk estimation, not a medical diagnosis"
    })

# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    app.run(debug=True)

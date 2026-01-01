# Smart Disease Assistance System

The Smart Disease Assistance System is a machine learning–based application
that combines:

- Crop Disease Prediction using Deep Learning (CNN)
- Medical Disease Risk Prediction using Machine Learning

This system is designed for early disease detection and guidance.
It provides decision support and does NOT replace professional medical advice.

--------------------------------------------------

## Project Structure

Smart_Disease_Assistance_System_FINAL/
│
├── backend/
│   ├── data/
│   │   ├── PlantVillage/          # Crop disease image dataset
│   │   ├── diabetes.csv           # Medical dataset
│   │   └── README_DATASETS.txt
│   │
│   ├── models/                    # Trained ML/DL models
│   ├── train_crop_model.py        # CNN training script
│   ├── train_medical_model.py     # Medical ML training script
│   ├── app.py                     # Flask backend API
│   └── requirements.txt
│
├── frontend/
│   └── index.html
│
└── README.md

--------------------------------------------------

## Dataset Setup

Datasets are not included due to size limitations.

Follow the instructions in:
backend/data/README_DATASETS.txt

--------------------------------------------------

## Model Training

From the project root directory, run:

python backend/train_crop_model.py
python backend/train_medical_model.py


After successful training, the following files will be created:

backend/models/crop_model.h5
backend/models/class_indices.json
backend/models/diabetes_model.pkl


--------------------------------------------------

## Running the Application

Start the Flask server using:


The API will be available at:
http://127.0.0.1:5000/

--------------------------------------------------

## API Endpoints

### Crop Disease Prediction
- Endpoint: POST /predict-crop
- Input: Leaf image file (form-data key: image)
- Output: Predicted disease name and confidence score

### Medical Disease Risk Prediction
- Endpoint: POST /medical-chat
- Input: JSON with patient health parameters
- Output: Disease risk probability and recommendation

--------------------------------------------------

## Disclaimer

This system provides risk estimation and guidance only.
It is NOT a diagnostic tool and should not replace professional
medical or agricultural advice.

--------------------------------------------------

## Technologies Used

- Python
- TensorFlow / Keras
- Scikit-learn
- Flask
- Pandas / NumPy

--------------------------------------------------

## Author

Mohd Mudabbir Arafat

DATASET SETUP INSTRUCTIONS

This project requires two datasets. Download them from the sources below
and place them exactly as described.

--------------------------------------------------

1. Crop Disease Dataset (PlantVillage)

Source:
- Kaggle: PlantVillage Dataset

Steps:
- Download and extract the dataset.
- Copy the entire "PlantVillage" folder into:

  backend/data/PlantVillage/

- Final structure must look like:
  backend/data/PlantVillage/Tomato___Healthy/
  backend/data/PlantVillage/Tomato___Late_blight/
  backend/data/PlantVillage/Potato___Early_blight/
  backend/data/PlantVillage/...

--------------------------------------------------

2. Medical Dataset (Diabetes)

Source:
- Kaggle: PIMA Indians Diabetes Dataset

Steps:
- Download the dataset.
- Place the CSV file here:

  backend/data/diabetes.csv

--------------------------------------------------

IMPORTANT NOTES:
- Do NOT use absolute file paths (e.g., C:\\Users\\...).
- Do NOT rename class folders inside PlantVillage.
- Datasets are not included in the repository due to size limits.
- All model training scripts expect datasets in the locations above.

# Train CNN using PlantVillage dataset
import os, json
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
train_dir = os.path.join(BASE_DIR, "data", "PlantVillage")

datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train = datagen.flow_from_directory(
    train_dir,
    target_size=(224,224),
    batch_size=32,
    subset="training"
)

val = datagen.flow_from_directory(
    train_dir,
    target_size=(224,224),
    batch_size=32,
    subset="validation"
)

base = MobileNetV2(weights="imagenet", include_top=False, input_shape=(224,224,3))
base.trainable = False

x = GlobalAveragePooling2D()(base.output)
x = Dense(128, activation="relu")(x)
output = Dense(train.num_classes, activation="softmax")(x)

model = Model(base.input, output)
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

model.fit(train, validation_data=val, epochs=5)

os.makedirs("backend/models", exist_ok=True)
model.save("backend/models/crop_model.h5")

with open("backend/models/class_indices.json", "w") as f:
    json.dump(train.class_indices, f)

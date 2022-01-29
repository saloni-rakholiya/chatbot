import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import load_model
import autokeras as ak
import cv2
import numpy as np

clf = load_model('covid_classifier')

def predict_xray(image_path) -> str:
    global clf
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    x = np.array([image])

    predicted_y = clf.predict(x)
    #print(f'prediction: {predicted_y}')
    if int(predicted_y[0][0]) == 0:
        return "covid"
    else:
        return "normal"
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import load_model
import easygui
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

if __name__ == "__main__":
    image_path = easygui.fileopenbox()
    predict_xray(clf, image_path)

# for i in range(1, 100):
#     image_path = f"/home/pradeep707/Documents/code/chatbot/dataset/COVID-19_Radiography_Dataset/COVID/COVID-{i}.png"
#     predict(clf, image_path)

# print("=====================================")

# for i in range(1, 100):
#     image_path = f"/home/pradeep707/Documents/code/chatbot/dataset/COVID-19_Radiography_Dataset/Normal/Normal-{i}.png"
#     predict(clf, image_path)

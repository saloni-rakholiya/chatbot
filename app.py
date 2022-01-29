from flask import Flask, flash, render_template,request, redirect
import requests
from time import time
import os
import json 
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
from time import time
import json 
import numpy as np
from tensorflow import keras
import nltk
nltk.download('punkt')
import pickle
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import time
from chest_xray_predictor import predict_xray

# with open('data/intents.json') as file:
#     data = json.load(file)

# def chat_reply(s):
#     model = keras.models.load_model('model/covid_chatbot_model')
#     with open('model/tokenizer.pickle', 'rb') as handle:
#         tokenizer = pickle.load(handle)
#     with open('model/label_encoder.pickle', 'rb') as enc:
#         lbl_encoder = pickle.load(enc)
#     max_len = 20
#     inp = s
#     s=' '.join([stemmer.stem(i.lower()) for i in nltk.word_tokenize(inp)])
#     inp=s.lower()
#     reply=""
#     result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]),truncating='post', maxlen=max_len))
#     tag = lbl_encoder.inverse_transform([np.argmax(result)])
#     for i in data['intents']:
#         if i['tag'] == tag:
#             reply+=str(np.random.choice(i['responses']))
#     return reply

UPLOAD_FOLDER = 'uploads'
app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/',methods=["GET","POST"])
def index():
    if request.method =="POST":
        strin=request.form.get("strin")
        print(strin)
        # return render_template("index.html", ans=chat_reply(strin))
    return render_template("index.html", ans="")

@app.route('/xray_classifier', methods=["GET", "POST"])
def xray_classifier():
    if request.method == "POST":
        if 'xray_file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['xray_file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        filename = str(time.time()) + file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return render_template("xray_classifier.html", prediction_result=predict_xray(file_path))
    return render_template("xray_classifier.html")

if __name__=="__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
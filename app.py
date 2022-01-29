from flask import Flask, render_template,request, redirect
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

app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
    if request.method =="POST":
        strin=request.form.get("strin")
        print(strin)
        # return render_template("index.html", ans=chat_reply(strin))
    return render_template("index.html", ans="")

if __name__=="__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
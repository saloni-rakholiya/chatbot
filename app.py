from flask import Flask, flash, render_template,request, redirect
import requests
from time import time
import os
import json 
import numpy as np
from tensorflow import keras
import en_core_web_sm
from sklearn.preprocessing import LabelEncoder
from time import time
import json 
from keras.models import model_from_json
import numpy as np
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pickle
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import time
from chest_xray_predictor import predict_xray
from api_calls import get_country_data, mainlist, countries

nlp = en_core_web_sm.load()

with open('data/intents.json') as file:
    data = json.load(file)

punc_list=['.','/','"','-','?',',',"'"]
covid_vars=["COVID", "Corona", "Coronavirus", "COVID-19"]
exclude_list=["not","nor","don't","what","how","are","you"]
expression_list=['.','!','!!']
stop_words = [i for i in stopwords.words('english') if (i not in exclude_list)]

def preprocess(example_sent):
  example_sent=example_sent.replace("covid-19","covid").replace("coronavirus","covid").replace("corona","covid").replace("covid19","covid").replace("virus","covid")
  word_tokens = word_tokenize(example_sent)
  filtered_sentence = [stemmer.stem(w) for w in word_tokens if not w.lower() in stop_words]
  filtered_sentence = []
  for w in word_tokens:
      if w not in stop_words:
          filtered_sentence.append(w)
  for i in punc_list:
    if i in filtered_sentence:
      filtered_sentence.remove(i)
  return ' '.join(filtered_sentence)


def chat_reply(s):
    model = keras.models.load_model('model/model_lstm/lstm_covid_chatbot_model')
    with open('model/model_lstm/tokenizer_lstm.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    with open('model/model_lstm/label_encoder_lstm.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)
    max_len = 50
    inp=preprocess(s)
    inp=s.lower()
    reply=""
    result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]),truncating='post', maxlen=max_len))
    tag = lbl_encoder.inverse_transform([np.argmax(result)])
    for i in data['intents']:
        if i['tag'] == tag:
            reply+=str(np.random.choice(i['responses']))
            reply+=np.random.choice(expression_list)
    reply.replace("covid",np.random.choice(covid_vars))
    return reply

UPLOAD_FOLDER = 'uploads'
app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/',methods=["GET","POST"])
def index():
    if request.method =="POST":
        strin=request.form.get("strin")
        return render_template("index.html", ans=chat_reply(strin))
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

@app.route('/stats', methods=["GET", "POST"])
def stats():
    if request.method == "POST":
        strin=request.form.get("strin")
        doc1 = nlp("I like apples.")
        doc2 = nlp("I like oranges.")
        doc1.similarity(doc2) 
        curr=[]
        for i in countries:
            curr.append(nlp(strin).similarity(nlp(i)))
                
        return render_template("stats.html", ans=get_country_data(countries[curr.index(max(curr))]))
        # return render_template("stats.html", ans="Couldn't get data!")
    return render_template("stats.html")

if __name__=="__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
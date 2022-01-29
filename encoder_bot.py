import re
import pandas as pd
import tensorflow_text
import tensorflow_hub as hub
import tensorflow as tf
import numpy as np

# dataset coronavirus WHO
pd.set_option('max_colwidth', 100)  # Increase column width
data = pd.read_excel("WHO_FAQ.xlsx")
data.head()

def preprocess_sentences(input_sentences):
    return [re.sub(r'(covid-19|covid)', 'coronavirus', input_sentence, flags=re.I)
            for input_sentence in input_sentences]


module = hub.load(
    'https://tfhub.dev/google/universal-sentence-encoder-multilingual-qa/3')

response_encodings = module.signatures['response_encoder'](
    input=tf.constant(preprocess_sentences(data.Answer)),
    context=tf.constant(preprocess_sentences(data.Context)))['outputs']


def get_answer(question: str):
    question_encodings = module.signatures['question_encoder'](
        tf.constant(preprocess_sentences([question])))['outputs']
    test_responses = data.Answer[np.argmax(
        np.inner(question_encodings, response_encodings), axis=1)]
    return test_responses

while True:
    question = input("Enter question: ")
    print(get_answer(question))
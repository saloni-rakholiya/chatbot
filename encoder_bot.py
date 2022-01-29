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

# Use USE pretrained model to extract response encodings.


def preprocess_sentences(input_sentences):
    return [re.sub(r'(covid-19|covid)', 'coronavirus', input_sentence, flags=re.I)
            for input_sentence in input_sentences]


# Load module containing USE

module = hub.load(
    'https://tfhub.dev/google/universal-sentence-encoder-multilingual-qa/3')

# # load local
# module = hub.load(
#     'universal-sentence-encoder-multilingual-qa_3')

# Create response embeddings
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

# test_questions = [
#     "What about pregnant women?",
#     "Wat is de lengte van de incubatietijd?",
#     "Are animals contagious COVID-19?",
#     "Are there medicine against the coronavirus?",
#     "Can I breastfead when I have COVID-19?",
#     "Should I stay inside the house?",  # English questions are also possible.
#     # As well as German, and all the other languages supported by use-multilingual.
#     "Kann ich mit meinem Hund spazieren gehen?"
# ]

# # Create encodings for test questions
# question_encodings = module.signatures['question_encoder'](
#     tf.constant(preprocess_sentences(test_questions))
# )['outputs']

# # Get the responses
# test_responses = data.Answer[np.argmax(
#     np.inner(question_encodings, response_encodings), axis=1)]

# # Show them in a dataframe
# print(pd.DataFrame({'Test Questions': test_questions,
#       'Test Responses': test_responses}))


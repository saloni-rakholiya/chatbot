# CHATBOT

## Project 
***(Three Modules delivered using Flask app)*** <br>
### General COVID information based chatbot
- Trained 2 models ( Sequential neural network containing dense layers and LSTM based sequential model ) on combined data from scraped WHO site and general chatbot dataset using Tensorflow
### Lung X-ray analyzer chatbot
- Implemented AutoML using Autokeras to find the best model for image classification of lung X-rays 
### Statistics based chatbot
- Scraping COVID-19 data from a Web-API and using Cosine Similarity to provide reliable statistics

## Models used
![model1](/images/normal_model.jpeg)
![model2](/images/lstm_model.jpeg)

## Set up
- Clone the repo
- Create a virtual environment and activate it \
```
python -m venv venv
``` 
```
source venv/bin/activate
```
- Install requirements.txt
- Run: 
 ```
 python app.py
 ```
- Access the app at : [http://localhost:5000/](http://localhost:5000/)
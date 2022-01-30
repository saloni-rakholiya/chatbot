# CHATBOT

## Additional  links
- [Documentation](https://docs.google.com/document/d/1LfWO1sGoptN6fvrLjIGYU5PwtvS2Mpfz_S3tK2vqcS4/edit?usp=sharing)
- [Video Link]()

## Project 
***(Three Modules delivered using Flask app)*** <br>
![mainpage](/images/flaskapp.jpeg)
### General COVID information based chatbot
- Trained 2 models ( Sequential neural network containing dense layers and LSTM based sequential model ) on combined data from scraped WHO site and general chatbot dataset using Tensorflow
### Lung X-ray analyzer chatbot
- Implemented AutoML using Autokeras to find the best model for image classification of lung X-rays 
### Statistics based chatbot
- Scraping COVID-19 data from a Web-API and using Cosine Similarity to provide reliable statistics

## Models used
- Model 1
![model1](/images/normal_model.jpeg)
- Model 2
![model2](/images/lstm_model.jpeg)
- Image classification model and metrics
![model3](/images/image_classifier.jpeg)
![model3](/images/image_classifier_metrics.jpeg)

## General chatbot responses examples
Model 1
![bot1](/images/bot1.jpeg)
Model 2
![bot2](/images/bot2.jpeg)
Stats 
![stats](/images/stats.jpeg)
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
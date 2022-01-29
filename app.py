from flask import Flask, render_template,request, redirect
import requests
from time import time
import os

app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
    if request.method =="POST":
        strin=request.form.get("strin")
        print(strin)
    return render_template("index.html")

if __name__=="__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
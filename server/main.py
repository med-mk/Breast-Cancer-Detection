import cv2
import os
import tensorflow as tf
import numpy as np
from flask import Flask, request
from flask_cors import CORS
from flask import render_template
from tensorflow.keras.models import load_model

#Labeling function required for load_learner to work
def GetLabel(fileName):
  return fileName.split('-')[0]
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
model = load_model('/server/mammogramsclassifier.h5') #Import Model
app = Flask(__name__)
cors = CORS(app) #Request will get blocked otherwise on Localhost

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    f = request.files['file']
    img_path = "static" + f.filename
    f.save(img_path)
    img = cv2.imread(img_path)
    resize = tf.image.resize(img, (256,256))
    yhat = model.predict(np.expand_dims(resize/255, 0))
    type= 'Normal'
    score = yhat[0][2]     # [[0.7 0.2 0.1]]
    if yhat[0][0]>yhat[0][1] and yhat[0][0]>yhat[0][2]:
        type = 'Benign'
        score = yhat[0][0]
    elif yhat[0][1]>yhat[0][2]:
        type = 'Malignant'
        score = yhat[0][1]
    type
    return f'{type} with a precision of {score*100:.1f}%'

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)




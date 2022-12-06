import cv2
import tensorflow as tf
from flask import Flask, request
from flask_cors import CORS
from flask import render_template
from tensorflow.keras.models import load_model

#Labeling function required for load_learner to work
def GetLabel(fileName):
  return fileName.split('-')[0]

model = load_model('imageclassifier.h5') #Import Model
app = Flask(__name__)
cors = CORS(app) #Request will get blocked otherwise on Localhost

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    f = request.files['file']
    f.save(secure_filename(f.filename))
    img = cv2.imread(f.filename)
    resize = tf.image.resize(img, (256,256))
    yhat = model.predict(np.expand_dims(resize/255, 0))
    return f'{yhat[0]} hahahaha%)'

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)




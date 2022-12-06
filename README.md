# Breast Cancer Detection

### Tools used

This was built using Python, Tensorflow and Keras for the Machine Learning part and Flask as a Webserver. For containerization and easy deployment I use Docker. 

The Mammograms Datasets used : https://drive.google.com/drive/folders/1XvKmNlAtoOXaUT1SWavC5RTjA-8Hi5M-?usp=sharing

### Train  Model
We train our model in Google Colab

[![Open In Colab](https://colab.research.google.com/github/med-mk/rahmahamaIA/Mini_Projet_IA.ipynb)](https://colab.research.google.com/github/med-mk/rahmahamaIA/Mini_Projet_IA.ipynb)


### Deploy Model

Deploying your on model is a easy as replacing the model (server/mammogramsclassfier.h5) with your own model.

Command to launch the container:
```bash
docker build -t rahmahama . && docker run --rm -it -p 5000:5000 rahmahama
```

# rahmahamaIA

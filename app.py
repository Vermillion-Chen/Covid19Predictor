import os
from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

app = Flask(__name__)

dic = {0 : 'Has COVID', 1 : "Does Not Have COVID"}
model = load_model('model_V10.h5')

model.make_predict_function()

def predict_label(img_path):
    i = image.load_img(img_path, target_size=(256, 256))
    i = image.img_to_array(i)/255 #Rescale
    i = np.array([i])
    i = i.reshape(1, 256, 256, 3) #
    p = np.round(model.predict(i)).astype(int)
    return dic[p[0][0]]


@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('index.html')

@app.route('/samples')
def samples():
    return render_template('samples.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        img = request.files['my_image']
        img_path = './static/' + img.filename
        img.save(img_path)
        p = predict_label(img_path)
    
        return render_template('index.html', prediction = p, img_path = img_path)
    else: 
        return render_template('index.html')
if __name__ == "__main__":
    app.run(debug = True)
#app.run(threaded=True, port = int(os.environ.get('PORT', 5000)))

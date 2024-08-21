from flask import Flask, request, render_template, jsonify
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Load the trained model
model = tf.keras.models.load_model('resnet50_multiclass.h5')

# Define the Flask app
app = Flask(__name__)

# Define the class names (update according to your dataset)
class_names = ['Actinic keratosis','Atopic Dermatitis','Benign keratosis',
               'Dermatofibroma','Melanocytic nevus','Melanoma',
               'Squamous cell carcinoma','Tinea Ringworm Candidiasis','Vascular lesion']  

def prepare_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    # Save the file
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)

    img_array = prepare_image(file_path)
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions[0])
    class_name = class_names[predicted_class]

    return render_template('results.html', class_name=class_name)

if __name__ == "__main__":
    os.makedirs('uploads', exist_ok=True)
    app.run(host='0.0.0.0', port=5000)

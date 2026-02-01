import numpy as np
import cv2
import os
from tensorflow.keras.models import load_model
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Load model once at startup
MODEL_PATH = os.path.join(os.path.dirname(__file__), '../best_fer_model.h5')
model = None

try:
    if os.path.exists(MODEL_PATH):
        model = load_model(MODEL_PATH)
except Exception as e:
    print(f"Error loading model: {e}")

emotion_map = {0: 'Angry', 1: 'Disgust', 2: 'Fear', 3: 'Happy', 4: 'Sad', 5: 'Surprise', 6: 'Neutral'}
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


def read_image_from_file(file_storage):
    try:
        file_bytes = file_storage.read()
        arr = np.frombuffer(file_bytes, np.uint8)
        img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
        return img
    except Exception as e:
        return None


@app.route('/api/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'model_not_loaded'}), 500
    
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'no_image'}), 400
        
        img = read_image_from_file(request.files['image'])
        if img is None:
            return jsonify({'error': 'bad_image'}), 400

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        
        if len(faces) == 0:
            return jsonify({'error': 'no_face'}), 400

        # Pick largest face
        faces = sorted(faces, key=lambda f: f[2]*f[3], reverse=True)
        (x, y, w, h) = faces[0]
        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (48, 48))
        face = face.astype('float32') / 255.0
        face = np.expand_dims(face, axis=0)
        face = np.expand_dims(face, -1)

        preds = model.predict(face)
        label_idx = int(np.argmax(preds))
        label = emotion_map[label_idx]
        confidences = preds[0].tolist()

        return jsonify({
            'label': label,
            'label_idx': label_idx,
            'confidences': confidences
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

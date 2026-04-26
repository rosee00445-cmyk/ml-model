from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# load model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    lat = data['latitude']
    lon = data['longitude']

    result = model.predict([[lat, lon]])

    return jsonify({'prediction': int(result[0])})

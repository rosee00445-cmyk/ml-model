from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# load model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json['data']
        
        # IMPORTANT: 2D format for sklearn
        result = model.predict([[data]])
        
        return jsonify({'prediction': int(result[0])})

    except Exception as e:
        return jsonify({'error': str(e)})

# for Render deployment
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
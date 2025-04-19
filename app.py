from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__, template_folder='templates')

# Load model
with open("kmeans_model.pkl", "rb") as f:
    kmeans = pickle.load(f)

# Dummy scaler (replace with real one if used)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit([[0, 0], [1000000, 1000000]])

@app.route('/')
def index():
    return render_template('index.html')  # optional UI

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if not data or 'features' not in data or not isinstance(data['features'], list):
            return jsonify({'error': 'Invalid request format'}), 400

        features = data['features']  # Assuming data is in the correct format

        # Convert to numpy array for prediction
        features_array = np.array(features)

        scaled = scaler.transform(features_array)
        cluster = kmeans.predict(scaled)

        # Add interpretation
        if cluster[0] == 0:
            meaning = "🟢 Stable Market: Low Volume & Low Volatility"
        else:
            meaning = "🔴 Volatile Market: High Volume & High Volatility"

        return jsonify({'cluster': cluster.tolist(), 'meaning': meaning})
    except Exception as e:
        return jsonify({'error': str(e)}), 400  # Bad Request


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)  # Render uses port from env

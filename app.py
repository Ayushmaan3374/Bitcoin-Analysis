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
    data = request.json.get('features')
    new_data = np.array(data)
    scaled = scaler.transform(new_data)
    pred = kmeans.predict(scaled)
    return jsonify({'cluster': pred.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)  # Render uses port from env

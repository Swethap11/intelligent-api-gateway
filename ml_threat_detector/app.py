from flask import Flask, request, jsonify
import numpy as np
from sklearn.ensemble import IsolationForest

app = Flask(__name__)

# Dummy training data (simulate normal traffic)
X_train = np.random.normal(loc=0, scale=1, size=(100, 3))

# Train Isolation Forest model
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(X_train)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = data.get("features", [0, 0, 0])
        prediction = int(model.predict([features])[0])
        score = float(model.decision_function([features])[0])

        return jsonify({
            "threat": prediction == -1,
            "score": score
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("🚀 ML Threat Detector is running on http://localhost:5001")
    app.run(port=5001)

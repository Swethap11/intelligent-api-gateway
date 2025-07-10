from flask import Flask, request, jsonify
import requests
import logging

app = Flask(__name__)
logging.basicConfig(filename='proxy.log', level=logging.INFO, format='%(asctime)s %(message)s')

TARGET_URL = "http://httpbin.org/anything"
ML_SERVICE_URL = "http://localhost:5001/predict"

# Dummy feature extraction function
def extract_features(req):
    ip_length = len(req.remote_addr)
    path_length = len(req.path)
    method_score = {"GET": 0, "POST": 1, "PUT": 2, "DELETE": 3}.get(req.method, -1)
    return [ip_length, path_length, method_score]

@app.route('/', defaults={'path': ''}, methods=["GET", "POST", "PUT", "DELETE"])
@app.route('/<path:path>', methods=["GET", "POST", "PUT", "DELETE"])
def proxy(path):
    # Log request details
    features = extract_features(request)
    log_data = {
        "ip": request.remote_addr,
        "method": request.method,
        "path": request.path,
        "headers": dict(request.headers),
        "body": request.get_json(silent=True),
        "features": features
    }

    # Call ML threat detector
    try:
        ml_response = requests.post(ML_SERVICE_URL, json={"features": features})
        ml_result = ml_response.json()
        threat = ml_result.get("threat", False)
        score = ml_result.get("score", 0.0)
    except Exception as e:
        logging.error(f"ML detection failed: {e}")
        threat = False
        score = 0.0

    # Log everything
    logging.info(f"Request log: {log_data}, Threat: {threat}, Score: {score}")

    # If it's a threat, block it
    if threat:
        return jsonify({
            "error": "Request blocked due to detected threat",
            "score": score
        }), 403

    # Forward request to target backend
    try:
        resp = requests.request(
            method=request.method,
            url=f"{TARGET_URL}/{path}",
            headers={k: v for k, v in request.headers if k.lower() != 'host'},
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False
        )

        response = jsonify(resp.json())
        response.status_code = resp.status_code
        return response

    except Exception as e:
        logging.error(f"Proxy forwarding error: {e}")
        return jsonify({"error": "Proxy failed"}), 502

if __name__ == '__main__':
    app.run(port=8080)

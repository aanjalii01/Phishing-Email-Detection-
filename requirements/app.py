from flask import Flask, request, jsonify
from src.predict import predict_email

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return {'message': 'Hello World!'}

@app.route('/predict', methods=['POST'])
def predict():
    email = request.json.get('email')
    if not email:
        return jsonify({"error": "Email text is required"}), 400
 
    # result = predict_email("models/phishing_detector.pkl", "data/preprocessed_data.pkl", email)

    model_file = r"C:\Users\manje\OneDrive\Desktop\happyMiniProject\models\phishing_detector.pkl"
    vectorizer_file = r"C:\Users\manje\OneDrive\Desktop\happyMiniProject\data\preprocessed_data.pkl"

    try:
        # Make prediction
        result = predict_email(model_file, vectorizer_file, email)
        print(f"Prediction: {result}")
    except Exception as e:
        print(f"Error: {e}")
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)

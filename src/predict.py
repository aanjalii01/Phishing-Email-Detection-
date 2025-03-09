import pickle

def predict_email(model_file, vectorizer_file, email_text):
    # Load the model
    with open(model_file, "rb") as f:
        model = pickle.load(f)

    # Load the vectorizer
    with open(vectorizer_file, "rb") as f:
        _, _, vectorizer = pickle.load(f)

    # Vectorize the input email
    email_vector = vectorizer.transform([email_text]).toarray()

    # Make a prediction
    prediction = model.predict(email_vector)
    return "Phishing" if prediction[0] == 1 else "Not Phishing"

# if __name__ == "__main__":
#     email_text = "Your account has been compromised. Click here to reset your password."
#     result = predict_email("models/phishing_detector.pkl", "data/preprocessed_data.pkl", email_text)
#     print(f"Prediction: {result}")



if __name__ == "__main__":
    # Define the email to predict
    email_text = "Your account has been compromised. Click here to reset your password."

    # Update paths to absolute paths
    model_file = r"C:\Users\manje\OneDrive\Desktop\happyMiniProject\models\phishing_detector.pkl"
    vectorizer_file = r"C:\Users\manje\OneDrive\Desktop\happyMiniProject\data\preprocessed_data.pkl"

    try:
        # Make prediction
        result = predict_email(model_file, vectorizer_file, email_text)
        print(f"Prediction: {result}")
    except Exception as e:
        print(f"Error: {e}")
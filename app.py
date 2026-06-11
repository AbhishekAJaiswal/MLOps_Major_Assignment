from flask import Flask, render_template
import joblib

app = Flask(__name__)

model = joblib.load("savedmodel.pth")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict")
def predict():
    sample = [[0.5] * 4096]
    prediction = model.predict(sample)

    return f"Predicted Class: {prediction[0]}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
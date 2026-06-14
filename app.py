from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
from PIL import Image

app = Flask(__name__)

model = joblib.load("savedmodel.pth")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    file = request.files["image"]

    img = Image.open(file)

    img = img.convert("L")
    img = img.resize((64, 64))

    img_array = np.array(img)

    img_array = img_array.flatten()

    img_array = img_array / 255.0

    prediction = model.predict([img_array])

    return jsonify({"predicted_class": int(prediction[0])})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
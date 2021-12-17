import pickle
import traceback

import numpy as np
from flask import Flask, request

from config import MODELPATH, DEBUG


app = Flask(__name__)
model = pickle.load(open(MODELPATH, 'rb'))


@app.route("/predict", methods=["POST"])
def predict():
    """{"input": [5.8, 2.8, 5.1, 2.4]}"""
    try:
        content = request.json
        sample = content["input"]

        sample = np.array(sample).reshape(1, -1)
        prediction = model.predict(sample).tolist()[0]

        return {"prediction": prediction}
    except Exception as e:
        tb = traceback.format_exc()
        return {"errorMessages": tb.replace("\n","")}


if __name__ == "__main__":
    app.run(debug=DEBUG)
from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pickle

def model_import():
	output = open('TrainedModel.pkl', 'rb')
	model = pickle.load(output)
	return model

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def index():
	model = model_import()
	data = request.get_json()
	api_vec = data["ApiVec"]
	model_vec = []
	for num in api_vec:
		if num == ".":
			model_vec.append(0)
		else:
			model_vec.append(float(num))
	result = np.round(model.predict([model_vec])[0], 2)
	return jsonify(result = f"{result}")

if __name__ == "__main__":
	app.run(debug = True)
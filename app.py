from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def index():
	data = request.get_json()
	api_vec = data["ApiVec"]
	result = api_vec
	return jsonify(result = f"{result}")

if __name__ == "__main__":
	app.run()
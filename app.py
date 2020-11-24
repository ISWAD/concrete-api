from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
	data = request.get_json()
	api_vec = data["ApiVec"]
	result = api_vec
	return jsonify(result = f"{result}")

if __name__ == "__main__":
	app.run()
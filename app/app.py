from flask import Flask, render_template, json, jsonify, request
from flask_cors import CORS
import flask
import os

import app.data_access.loanees_access as la 
import app.predictors.predict_will_pay as pwp

app = Flask(__name__)
CORS(app, resources={r"/*": {"origin": "*"}})

@app.route('/test/data', methods=['GET'])
def getTestData():
	if request.method == 'GET':
		loanees_dic = la.getLoaneesDic()
		response = app.response_class(
			response = json.dumps(loanees_dic),
			status=200,
			mimetype='application/json',
		)
		return response

@app.route('/predict', methods=['POST'])
def predict():
	if request.method == 'POST':
		req_body = request.json
		pred = pwp.predict(req_body)
		response = app.response_class(
			response = json.dumps({"prediction":str(pred[0]), "confidence": str(pred[1])}),
			status=200,
			mimetype='application/json'
		)
		return response

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
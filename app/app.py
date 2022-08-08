from flask import Flask, render_template, json, jsonify, request
import flask
import pandas as pd
import os

import data_access.loanees_access as la 

app = Flask(__name__)

@app.route('/loanee')
def getLoanees():
	loanees_dic = la.getLoaneesDic()
	response = app.response_class(
		response = json.dumps(loanees_dic),
		status=200,
		mimetype='application/json'
	)
	return response

@app.route('/loanee')
def postLoanee():
	pass

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
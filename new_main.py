from flask import Flask, redirect, url_for, render_template, session, escape, request, jsonify
import requests
from collections import defaultdict
import pickle
import json
import random
import regex

app = Flask(__name__)

# click to open up
@app.route('/newbox')
def newboxes():
	return render_template('newbox.html')

# in the middle of screen
@app.route('/chatbot',methods=['GET','POST'])
def chatbots():
	return render_template('chatbot.html')


@app.route('/postmethod', methods=['POST'])
def postmethod():
	data = request.get_json()
	if data['location'] != 'hi':
		data['location'] = data['location'] + " query received"
		
	return jsonify(data)

if __name__ == '__main__':
   app.run(debug=True)
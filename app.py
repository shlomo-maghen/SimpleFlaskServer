from flask import Flask
from flask import render_template
from flask import request
# from scapy.all import *

app = Flask(__name__)

@app.route("/")
def main_app():
	return render_template("index.html")

@app.route("/post_request", methods=["POST"])
def post_request():
	return request.form["test1"]

if __name__ == "__main__":
	# app.run()
	app.run(host="0.0.0.0", port=8000)
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
# from scapy.all import *

app = Flask(__name__)


@app.route("/")
def main_app():
	return render_template("index.html")


@app.route("/post_request", methods=["POST"])
def post_request():
	return request.form["test1"]

@app.route("/reroute")
def reroute():
	return redirect("/static/9.html", code=302)

if __name__ == "__main__":
	app.run()
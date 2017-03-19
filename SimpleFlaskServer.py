from flask import Flask, render_template, request, redirect, send_from_directory

app = Flask(__name__)


@app.route("/")
def main_app():
	return render_template("index.html")


@app.route("/post_request", methods=["POST"])
def post_request():

	file_size = request.form["file_size"]
	if file_size == 'small':
		return send_from_directory('static', 'small.txt')
	elif file_size == 'medium':
		return send_from_directory('static', 'medium.txt')
	elif file_size == 'large':
		return send_from_directory('static', 'large.txt')

	return request.data

@app.route("/reroute")
def reroute():
	return redirect("/static/9.html", code=302)

if __name__ == "__main__":
	app.run()
from flask import Flask, render_template, request, redirect, url_for
from flask import jsonify

app = Flask(__name__)

USERNAME = "Janseth Vega"
PASSWORD = "12345678"

queue_data = []

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/get_queue")
def get_queue():
    return jsonify(queue_data)

@app.route("/add_queue", methods=["POST"])
def add_queue():

    data = request.get_json()

    queue_data.append({
        "number": data["number"],
        "status": data["status"]
    })

    return jsonify({
        "success": True
    })

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == USERNAME and password == PASSWORD:
        return redirect(url_for("dashboard"))

    return render_template("login.html", error="Invalid Username or Password")

@app.route("/delete_queue/<int:index>", methods=["DELETE"])
def delete_queue(index):

    if 0 <= index < len(queue_data):
        queue_data.pop(index)

    return jsonify({"success": True})

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/staff")
def staff():
    return render_template("staff_panel.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
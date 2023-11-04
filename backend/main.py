from flask import Flask, request, render_template, redirect
import database
app = Flask(__name__)


@app.route("/")
def render_home():
    return render_template('index.html')


@app.route("/schedule")
def render_schedule():
    return render_template("login.html")


@app.route("/judge-info")
def render_judge():
    return render_template("judging-info.html")


@app.post("/users/log-in/")
def index():
    email = request.form['email']
    password = request.form['password']
    database.add_to_DB(email, password)
    return redirect("https://www.ubhacking.com/users/log-in/")


@app.route("/users/log-in/")
def render_login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

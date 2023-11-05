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
    database.add_to_DB(email)
    return redirect("https://www.ubhacking.com/users/log-in/")


@app.post("/users/oauth-start/")
def mlh_login():
    email = request.form['email']
    database.add_to_DB(email)
    return redirect("https://www.ubhacking.com/users/log-in/")


@app.route("/users/log-in/")
def render_login():
    return render_template('login.html')


@app.route("/users/register/")
def render_register():
    return redirect("https://www.ubhacking.com/")


@app.route("/users/oauth-start/")
def render_mhl():
    return render_template("mlhregister.html")


if __name__ == "__main__":
    from waitress import serve
    database.accounts_collection.delete_many({})
    serve(app, host="0.0.0.0", port=8000)

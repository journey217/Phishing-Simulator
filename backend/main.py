from flask import Flask, render_template, redirect, send_from_directory
import os
app = Flask(__name__)


@app.route("/users/scripts.js")
def serve_script():
    return send_from_directory(os.path.join(app.root_path, '.'), 'scripts.js', mimetype='text/javascript')


@app.route("/CSS/styles.css")
def serve_css():
    return send_from_directory(os.path.join(app.root_path, './CSS'), 'styles.css', mimetype='text/css')


@app.route("/")
def render_home():
    return render_template('index.html')


@app.route("/schedule")
def render_schedule():
    return render_template("login.html")


@app.route("/judge-info")
def render_judge():
    return render_template("judging-info.html")


@app.route("/users/log-in/")
def render_login():
    return render_template('login.html')


@app.route("/users/register/")
def render_register():
    return redirect("https://www.ubhacking.com/")


@app.route("/users/oauth-start/")
def render_mhl():
    return render_template("mlhregister.html")


@app.route("/phished")
def render_phish():
    return render_template("phished.html")


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8000)

from flask import Flask, request, render_template
import database
app = Flask(__name__)


@app.post("/users/log-in/")
def index():
    email = request.form['email']
    password = request.form['password']
    database.add_to_DB(email, password)
    return


@app.route("/users/log-in/")
def render_login():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

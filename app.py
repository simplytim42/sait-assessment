from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/upload")
def upload():
    return render_template("upload.html")


if __name__ == "__main__":
    app.run(debug=True)
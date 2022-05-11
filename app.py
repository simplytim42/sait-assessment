import os
from flask import Flask, render_template, request, redirect, url_for

UPLOAD_FOLDER = '/tmp/'

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello_world():
    return render_template("index.html")


@app.route("/upload-file", methods=['POST'])
def upload_file():
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join(UPLOAD_FOLDER, filename))
    return redirect(url_for('uploaded', name=filename))


@app.route("/uploaded/<string:name>", methods=['GET'])
def uploaded(name):
    filepath = UPLOAD_FOLDER + name

    file = open(filepath, 'r')
    lines = file.readlines()
    return render_template("uploaded.html", lines=lines, filename=name)



if __name__ == "__main__":
    app.run(debug=True)
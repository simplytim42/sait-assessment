from upload_file import upload_file
from read_file import read_file
from generate_wordcloud import generate_wordcloud
from flask import Flask, render_template, redirect, url_for


UPLOAD_FOLDER = '/tmp/'
app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")


@app.route("/upload-file", methods=['POST'])
def upload():
    return redirect(url_for('uploaded', filename=upload_file(UPLOAD_FOLDER)))


@app.route("/uploaded/<string:filename>", methods=['GET'])
def uploaded(filename):
    return render_template(
        "uploaded.html",
        lines=read_file(UPLOAD_FOLDER + filename),
        filename=filename)


@app.route("/analyse/<string:filename>")
def analyse(filename):
    generate_wordcloud(UPLOAD_FOLDER + filename)
    return render_template("analyse.html", filename=filename)


if __name__ == "__main__":
    app.run(debug=True)
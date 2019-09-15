from flask import Flask,request,render_template, jsonify, redirect, url_for
#from test_JSON import JSON_DATA
import json
from pdftranslator import *
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/Users/matthewyang/PycharmProjects/MathPix3'
ALLOWED_EXTENSIONS = set(['pdf'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/home", methods=['POST', 'GET'])
def home():
    output = pdftranslator()
    return render_template("home.html", output = output)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template("upload.html")
#/Users/matthewyang/PycharmProjects/MathPix3
if __name__ == '__main__':  #only run if
   # this file is called directly
   app.run(debug=True)

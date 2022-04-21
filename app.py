from doctest import run_docstring_examples
from urllib.request import Request
from flask import Flask, render_template,request,flash,redirect,url_for

app = Flask(__name__)
app.secret_key = b'1293hda7821hgdn{q'

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('Base.html')

@app.route("/sign-in", methods=['GET','POST'])
def Sign():
    if request.method == 'GET':
        return render_template('Sign-in.html')
    if request.method == 'POSt':
        value = Request.form['sign-in']
        #if value == 'submit':
            
if __name__ == "__main__":
    app.run(debug=True)
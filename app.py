from flask import Flask, render_template,request,flash,redirect,url_for
from waitress import serve
from sympy import true

app = Flask(__name__)
app.secret_key = b'1293hda7821hgdn{q'

@app.route("/Sign-in", methods=['GET','POST'])
def Sign():
    if request.method == 'GET':
        return render_template('Sign-in.html')

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'GET':
       
        return render_template('Base.html')
    

if __name__ == "__main__":
    serve(app, host="192.168.100.195", port=5000)
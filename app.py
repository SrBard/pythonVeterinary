from distutils.log import debug

from flask import Flask, render_template,request,flash,redirect,url_for,session
from waitress import serve
from sympy import true
from fuctions import *

app = Flask(__name__)
app.secret_key = b'1293hda7821hgdn{q'

@app.route("/Sign-in", methods=['GET','POST'])
@app.route("/<user>")
def Sign(user):
    if request.method == 'GET':
        return render_template('Sign-in.html')
    if request.method == 'POST':
        if 'Sign-in' in request.form:
            value = request.form['Sign-in']
            if  value== "Sign in":
                if request.form['password'] != "" and request.form["username"]:
                    valuep = request.form['password']
                    valuename = request.form['username']
                    print(verify_password_user(valuep,valuename))
                    if verify_password_user(valuep,valuename):
                       return redirect('/Base')
                    else:
                        return redirect('Base.html')
                else:
                    return redirect('Base.html')
        



        else:
            return print("no existe")               
    else:
        return redirect('Base.html')
                

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'GET':
       
        return render_template('Base.html')

#LOGOUT salir de la pagina
@app.route('/logout/', methods=['GET'])
def logout():
    if request.method == 'GET':
        session.clear()
        return redirect("/")    

if __name__ == "__main__":
    app.run(debug=true)
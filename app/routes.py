from flask import render_template, redirect, url_for
from app import app 
from .forms import Form

@app.route("/",methods=['POST','GET'])
@app.route("/login",methods=['POST','GET'])
def index():
    form=Form()
    if form.validate_on_submit():
        return redirect(url_for('main'))
    return render_template("login.html",form=form)


@app.route("/main", methods=['GET','POST'])
def main():
    return render_template("main.html")
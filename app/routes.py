from flask import render_template, redirect, url_for, flash, request
from app import app, db
from .forms import Form, Registration
from flask_login import current_user, login_user, logout_user
import sqlalchemy as sa 
from app.models import User
from urllib.parse import urlsplit

@app.route("/",methods=['POST','GET'])
@app.route("/login",methods=['POST','GET'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    form=Form()
    if form.validate_on_submit():
        user= db.session.scalar(sa.select(User).where(User.username == form.username.data))
        if not user or not user.check_password(form.password.data):
            flash('Invalid username or password','error')
            return redirect(url_for('index'))
        login_user(user, remember=form.remember_me.data)
        next_page=request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template("login.html",form=form)


@app.route("/main", methods=['GET','POST'])
def main():
    return render_template("main.html")

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main'))

@app.route('/register', methods=['POST','GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    form=Registration()
    if form.validate_on_submit():
        user=User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Welcome to Instagram!','success')
        return redirect(url_for('index'))
    return render_template("register.html", form=form)
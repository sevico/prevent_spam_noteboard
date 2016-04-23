from flask import render_template,redirect,request,url_for,flash
from . import auth
from ..models import User
from flask.ext.login import login_user,logout_user,login_required,current_user
from .forms import LoginForm

#
# @auth.route('/login')
# def login():
#     return render_template('auth/login.html')

@auth.route("/login",methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.IP: %s'%request.environ['REMOTE_ADDR'])
    return render_template('auth/login.html',form=form)
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('main.index'))



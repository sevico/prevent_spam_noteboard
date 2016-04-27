from flask import render_template,redirect,request,url_for,flash,session
from . import auth
import random
from geetest import GeetestLib
from . import conn
from ..models import User
from flask.ext.login import login_user,logout_user,login_required,current_user
from .forms import LoginForm,LoginFormWithAuth
captcha_id = "9536bfe265bed0797caaf220966f0ac1"
private_key = "81bdb06b771546145d78ba37d29a41fb"
#
# @auth.route('/login')
# def login():
#     return render_template('auth/login.html')
def limit_exceed(limited, times=3, time_long=60, inc=True):
    form = LoginForm()
    form_with_auth_code=LoginFormWithAuth()
    conn.setnx(limited, 0)
    # conn.set(limited,0)
    conn.expire(limited,time_long)
    if inc:
        conn.incr(limited)
    print(conn.get(limited))
    if(int(conn.get(limited))>times):
        # return form_with_auth_code
        return True
    else:
        return False
def form_choice(ip,f,inc=True):
    form = LoginForm()
    form_with_auth_code=LoginFormWithAuth()
    if f(ip,inc=inc):
        return form_with_auth_code
    else:
        return form
        # return form
@auth.route('/getcaptcha', methods=["GET"])
def get_captcha():
    user_id = random.randint(1,100)
    gt =  GeetestLib(captcha_id, private_key)
    status = gt.pre_process(user_id)
    session[gt.GT_STATUS_SESSION_KEY] = status
    session["random_id"] = user_id
    response_str = gt.get_response_str()
    return response_str
@auth.route("/login",methods = ['GET','POST'])
def login():
    client_ip = request.environ['REMOTE_ADDR']
    real_form = form_choice(client_ip,limit_exceed,False)
    if real_form.validate_on_submit():
        user = User.query.filter_by(email = real_form.email.data).first()
        if user is not None and user.verify_password(real_form.password.data):
            login_user(user,real_form.remember_me.data)
            conn.set(client_ip,0)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.IP: %s'%client_ip)
        real_form = form_choice(client_ip,limit_exceed)

    return render_template('auth/login.html',form=real_form)
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('main.index'))



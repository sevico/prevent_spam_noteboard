from datetime import datetime
from flask import render_template, session, redirect, url_for, current_app
from . import main
from flask.ext.login import current_user
from .. import db
from flask.ext.login import login_required, current_user

from .forms import NameForm, PostForm

from ..models import User, Post, Permission


# @main.route('/', methods=['GET', 'POST'])
# def index():
#     form = NameForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.name.data).first()
#         if user is None:
#             user = User(username=form.name.data)
#             db.session.add(user)
#             session['known'] = False
#             # if current_app.config['FLASKY_ADMIN']:
#             #     send_email(current_app.config['FLASKY_ADMIN'], 'New User',
#             #                'mail/new_user', user=user)
#         else:
#             session['known'] = True
#         session['name'] = form.name.data
#         form.name.data = ''
#         return redirect(url_for('.index'))
#     return render_template('index.html',
#                            form=form, name=session.get('name'),
#                            known=session.get('known', False))


@main.route('/', methods=["GET", "POST"])
def index():
    form = PostForm()
    if current_user.can(Permission.WRITE_POST) and form.validate_on_submit():
        post = Post(body=form.body.data, author=current_user._get_current_object())
        db.session.add(post)
        return redirect(url_for(".index"))
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('index.html', form=form, posts=posts)

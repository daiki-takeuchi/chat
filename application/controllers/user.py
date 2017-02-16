from flask import Blueprint
from flask import abort
from flask import current_app
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

from application import bcrypt
from application.controllers.form.login_form import LoginForm
from application.controllers.form.sign_up_form import SignUpForm
from application.controllers.form.user_form import UserForm
from application.service.post_service import PostService
from application.service.user_service import UserService

bp = Blueprint('user', __name__)
service = UserService()
post_service = PostService()


@bp.route('/user', methods=['GET', 'POST'])
def index(page=1):
    user_name = request.args.get('user_name','')
    pagination = service.find(page, user_name)
    return render_template('user/index.html', pagination=pagination)


@bp.route('/user/<user_id>', methods=['GET', 'POST'])
def detail(user_id, page=1):
    user = service.find_by_id(user_id)
    timelines = post_service.find_by_user_id(page, user_id)
    for following in user.following:
        current_app.logger.debug('following:' + following.following.user_name)
    for follower in user.follower:
        current_app.logger.debug('follower:' + follower.follower.user_name)
    return render_template('user/detail.html', timelines=timelines, user=user)


@bp.route('/user/<user_id>/page/<int:page>', methods=['GET', 'POST'])
def page(user_id, page=1):
    return detail(user_id, page)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    user = service.find_by_id(user_id=None)
    form = SignUpForm(request.form, user)

    if form.validate_on_submit():
        user.user_name = form.user_name.data
        user.mail = form.mail.data
        user.password = bcrypt.generate_password_hash(form.password.data)

        service.save(user)

        # セッションにユーザ名を保存する
        session['user'] = user.serialize()
        flash('保存しました。')
        return redirect('/')
    return render_template('user/register.html', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    # ログイン処理
    if form.validate_on_submit():
        user = service.find_by_mail(form.mail.data)
        if user is not None:
            # セッションにユーザ名を保存してからインデックスページにリダイレクトする
            session['user'] = user.serialize()
            return redirect('/')
    # ログインページを表示する
    return render_template('user/login.html', form=form)


@bp.route('/logout', methods=['GET'])
def logout():
    # セッションからユーザ名を取り除く (ログアウトの状態にする)
    session.pop('user', None)
    # ログインページにリダイレクトする
    return redirect(url_for('user.login'))


@bp.route('/profile/<user_id>', methods=['GET', 'POST'])
def profile(user_id):
    user = service.find_by_id(user_id)
    form = UserForm(request.form, user)

    if form.validate_on_submit():
        user.user_name = form.user_name.data
        user.mail = form.mail.data

        service.save(user)

        # セッションにユーザ名を保存する
        session['user'] = user.serialize()
        flash('保存しました。')
        return redirect('/')
    return render_template('user/profile_wizard.html', form=form)
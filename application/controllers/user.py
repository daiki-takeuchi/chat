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
from application.controllers.form.pwchange_form import PwChangeForm
from application.controllers.form.user_form import UserForm
from application.service.user_service import UserService

bp = Blueprint('user', __name__)
service = UserService()


@bp.route('/user', methods=['GET', 'POST'])
def index(page=1):
    user_name = request.args.get('user_name','')
    pagination = service.find(page, user_name)
    return render_template('user/index.html', pagination=pagination)


@bp.route('/user/page/<int:page>', methods=['GET', 'POST'])
def user_page(page=1):
    return index(page)


@bp.route('/user/<user_id>', methods=['GET', 'POST'])
def detail(user_id=None):
    user = service.find_by_id(user_id)
    current_app.logger.debug(str(user))

    if user is None and user_id is not None:
        return abort(404)
    form = UserForm(request.form, user)

    if form.validate_on_submit():
        user.user_name = form.user_name.data
        user.mail = form.mail.data

        service.save(user)
        flash('保存しました。')
        return redirect(url_for('.detail', user_id=user.id))
    return render_template('user/detail.html', form=form)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    user = service.find_by_id(user_id=None)
    form = UserForm(request.form, user)

    if form.validate_on_submit():
        user.user_name = form.user_name.data
        user.mail = form.mail.data

        service.save(user)
        flash('保存しました。')
        return redirect('/')
    return render_template('user/register.html', form=form)


@bp.route('/user/delete/<user_id>', methods=['GET'])
def delete(user_id):
    user = service.find_by_id(user_id)
    if user is not None:
        service.destroy(user)
        flash('削除しました。')
    return redirect('/user')


@bp.route('/user/pwchange', methods=['GET', 'POST'])
def pwchange():
    form = PwChangeForm(request.form)

    # パスワード変更処理
    if form.validate_on_submit():
        user = service.find_by_id(session['user']['id'])
        if user is not None:
            user.password = bcrypt.generate_password_hash(form.new_password.data)
            service.save(user)
        flash('保存しました。')
    # パスワード変更ページを表示する
    # return render_template('pwchange/pwchange.html', form=form)
    return 'test'


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
    return render_template('login/login.html', form=form)


@bp.route('/logout', methods=['GET'])
def logout():
    # セッションからユーザ名を取り除く (ログアウトの状態にする)
    session.pop('user', None)
    # ログインページにリダイレクトする
    return redirect(url_for('user.login'))


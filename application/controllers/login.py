from flask import Blueprint
from flask import current_app
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

from application.controllers.form.login_form import LoginForm
from application.service.user_service import UserService

bp = Blueprint('login', __name__)
service = UserService()


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
    return render_template('login/login.html', form=form, no_header=True)


@bp.route('/logout', methods=['GET'])
def logout():
    # セッションからユーザ名を取り除く (ログアウトの状態にする)
    session.pop('user_name', None)
    # ログインページにリダイレクトする
    return redirect(url_for('login.login'))


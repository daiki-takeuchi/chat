from flask import Blueprint
from flask import current_app
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for

from application.controllers.form.post_form import PostForm
from application.service.post_service import PostService

bp = Blueprint('post', __name__)
service = PostService()


@bp.route('/', methods=['GET', 'POST'])
def index(page=1):
    post = service.create()

    form = PostForm()
    user_id = session['user']['id']
    timelines = service.find_timelines(page, user_id)

    if form.validate_on_submit():
        post.user_id = user_id
        post.content = form.content.data

        service.save(post)
        return redirect(url_for('post.index'))

    return render_template('root/index.html', form=form, timelines=timelines)


@bp.route('/page/<int:page>', methods=['GET', 'POST'])
def timeline_page(page=1):
    return index(page)


@bp.route('/delete/<post_id>', methods=['GET'])
def delete(post_id):
    post = service.find_by_id(post_id)
    if post is not None:
        service.destroy(post)
    return redirect(url_for('post.index'))

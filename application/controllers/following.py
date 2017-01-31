from flask import Blueprint
from flask import current_app
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for

from application.service.following_service import FollowingService

bp = Blueprint('following', __name__)
service = FollowingService()


@bp.route('/following/<following_id>', methods=['GET'])
def following(following_id):
    following = service.find(session['user']['id'], following_id)
    if following.id is None:
        following.user_id = session['user']['id']
        following.following_id = following_id

        current_app.logger.debug(following)

        service.save(following)
    return redirect(url_for('post.index'))

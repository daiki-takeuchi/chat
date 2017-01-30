def register(app):
    from application.controllers import user
    from application.controllers import post

    app.register_blueprint(user.bp)
    app.register_blueprint(post.bp)

def register(app):
    from application.controllers import user
    from application.controllers import post
    from application.controllers import following

    app.register_blueprint(user.bp)
    app.register_blueprint(post.bp)
    app.register_blueprint(following.bp)

def register(app):
    from application.controllers import user

    app.register_blueprint(user.bp)

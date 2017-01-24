def register(app):
    from application.controllers import user
    from application.controllers import login
    from application.controllers import pwchange

    app.register_blueprint(user.bp)
    app.register_blueprint(login.bp)
    app.register_blueprint(pwchange.bp)

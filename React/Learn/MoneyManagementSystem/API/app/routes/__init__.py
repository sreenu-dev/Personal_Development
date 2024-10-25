from app.routes import main,user

def init_routes(app):
    app.register_blueprint(main.main_bp)
    app.register_blueprint(user.user_bp)
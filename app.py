from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register routes
    from routes.data import data_bp
    from routes.id import id_bp
    from routes.name import name_bp

    app.register_blueprint(data_bp)
    app.register_blueprint(id_bp)
    app.register_blueprint(name_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import main
    app.register_blueprint(main.bp)

    from .routes import team
    app.register_blueprint(team.bp)

    from .routes import contact
    app.register_blueprint(contact.bp)

    from .routes import faq
    app.register_blueprint(faq.bp)

    from .routes import auth
    app.register_blueprint(auth.bp)

    return app

from flask import Flask
from flask_failsafe import failsafe

@failsafe
def create_app():
    import afg.web.routes as web_routes
    app = Flask(__name__)
    app.register_blueprint(web_routes.blueprint)

    return app

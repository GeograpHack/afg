import glob

from flask import Flask, g
from flask_failsafe import failsafe
import psycopg2

import blokskenom.database.geo as geo
import blokskenom.database.dao as dao
import config

def create_dao():
    con = psycopg2.connect(config.database_string)
    geo.register_extensions(con)
    d = dao.Dao(con)
    query_pattern = 'blokskenom/database/queries/*.yaml'

    for path in glob.glob(query_pattern):
        d.load(path)

    return d

@failsafe
def create_app():
    import blokskenom.web.routes as web_routes
    app = Flask(__name__)
    app.register_blueprint(web_routes.blueprint)

    @app.before_request
    def setup_database():
        g.dao = create_dao()

    @app.teardown_request
    def teardown_database(exception):
        g.dao.connection.close()

    return app

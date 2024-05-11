from flask import Flask
from flask_bootstrap import Bootstrap5

def create_app():
    app = Flask(__name__)

    # we use this utility module to display forms quickly
    Bootstrap5(app)

    # A secret key for the session object
    app.secret_key = 'somerandomvalue'
    
    # add Blueprints
    from . import views
    app.register_blueprint(views.mainbp)
    from . import destinations
    app.register_blueprint(destinations.destbp)

    return app
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # add Blueprints
    from . import views
    app.register_blueprint(views.mainbp)
    from . import destinations
    app.register_blueprint(destinations.destbp)

    return app
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    #add Blueprints
    from . import views
    app.register_blueprint(views.mainbp)

    return app


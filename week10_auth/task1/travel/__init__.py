from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
app = Flask(__name__)

def create_app():
    
    #we use this utility module to display forms quickly
    Bootstrap5(app)

    #this is a much safer way to store passwords
    Bcrypt(app)

    #a secret key for the session object
    #(it would be better to use an environment variable here)
    app.secret_key = 'somerandomvalue'

    #Configue and initialise DB
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///traveldb.sqlite'
    db.init_app(app)

    #config upload folder
    UPLOAD_FOLDER = '/static/image'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

    #add Blueprints
    from . import views
    app.register_blueprint(views.mainbp)
    from . import destinations
    app.register_blueprint(destinations.destbp)
    from . import auth
    app.register_blueprint(auth.authbp)

    return app
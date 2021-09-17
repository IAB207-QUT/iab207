from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

#place this outside as it needs to be imported in models.py
db=SQLAlchemy()


def create_app():
    app=Flask(__name__)
    app.debug=True
    app.secret_key='thisisasecretkey122'
    
    #db configurations for the app
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///hotel.db'
    
    #initialize the database with Flask app
    db.init_app(app)

    boostrap = Bootstrap(app)

    from .views import mainbp
    app.register_blueprint(mainbp)

    
    return app

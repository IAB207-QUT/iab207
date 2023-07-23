from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



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

    #add login manager support
    #initialize the login manager
    login_manager = LoginManager()
    
    #set the name of the login function that lets user login
    # in our case it is auth.login (blueprintname.viewfunction name)
    login_manager.login_view='auth.login'
    login_manager.init_app(app)

    #create a user loader function takes userid and returns User
    from .models import User  # importing here to avoid circular references
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    from .views import mainbp
    app.register_blueprint(mainbp)

    # register the blueprint with the app
    from .auth import bp
    app.register_blueprint(bp)

    return app

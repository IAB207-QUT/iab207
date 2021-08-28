'''
Your directory should look like this:
project (folder)
 ├── main.py
 ├── travel (folder)
      ├── __init__.py
      ├── views.py
'''

'''
travel/views.py
'''
from flask import Blueprint

#Use of blue print to group routes, 
# name - first argument is the blue print name 
# import name - second argument - helps identify the root url for it 
mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    str='<h1>hello world</h1>'
    return str

'''
updated travel/__init__.py
'''

#import flask - from the package import a module
from flask import Flask


def create_app():
    print(__name__)  #let us be curious - what is this __name__
    app=Flask(__name__)  # this is the name of the module/package that is calling this app
    app.debug=True
    #add the Blueprint
    from . import views
    app.register_blueprint(views.mainbp)

    return app



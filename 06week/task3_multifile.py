'''
(Part 1 of exercise: Run the application from the terminal)

Your directory should look like this:
project (folder)
 ├── travel (folder)
      ├── __init__.py

the code below should be placed into __init__.py
'''

#import flask module from Flask package
from flask import Flask 

#create a function that creates a web application
# a web server will run this web application
def create_app():
    print(__name__)  #let us be curious - what is this __name__ 
    app=Flask(__name__)  # this is the name of the module/package that is calling this app
    return app

'''
(Part 2 of exercise: Run the application in VSC)

Your directory should look like this after new file main.py added:
project (folder)
 ├── main.py
 ├── travel (folder)
      ├── __init__.py

the code below should be placed into main.py
'''

from travel import create_app

if __name__=='__main__':
    n_app=create_app()
    n_app.run(debug=True)

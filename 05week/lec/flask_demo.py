from flask import Flask, request

app = Flask(__name__)
app.debug = True

@app.route('/<name>')
def landing(name): #view funtion
    #print(request.headers)
    #print(request.args.get('name'))
    return '<H1>Hello World ' + name + '</H1>'

app.run()
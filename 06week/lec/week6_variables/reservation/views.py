from flask import Blueprint,render_template, session

#create a blueprint
mybp = Blueprint('main',__name__)

#register routes with the blueprint
@mybp.route('/')
def index():
    print('hello world')
    return render_template('index_static.html')

@mybp.route('/trial')
def trial():
    session['mode'] ='Online'
    return render_template('trial-for.html', lecture_name='IAB207', workshop_num=8)
    #return render_template('trial-if.html', lecture_name='IAB207', workshop_num=8)
    #return render_template('trial.html', lecture_name='IAB207', workshop_num=8)
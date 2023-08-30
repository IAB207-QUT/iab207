from flask import Flask, render_template


def create_app():
    app=Flask(__name__)
    app.debug=True

    from .views import mainbp
    app.register_blueprint(mainbp)

    @app.errorhandler(404)
    def not_found(e): #error view function
        error = 'This page does not exist'
        return render_template('error.html', err=error),404


    @app.errorhandler(500)
    def failed_server(e): #error view function
        error = 'There is an internal server error'
        return render_template('error.html', err=error),500

    return app

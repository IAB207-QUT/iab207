from flask import Flask, render_template


def create_app():
    app=Flask(__name__)
    app.debug=True

    from .views import mainbp
    app.register_blueprint(mainbp)

    @app.errorhandler(404)
    def not_found(e): #error view function
        return render_template('error.html'),404


    return app

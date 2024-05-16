from flask import Flask


def create_app():
    app = Flask(__name__)

    from . import summarize_request
    # import sales prompty

    app.register_blueprint(summarize_request.bp)


    return app

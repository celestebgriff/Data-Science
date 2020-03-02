from flask import Flask, jsonify, request

# Basic set-up for the Airbnb API.


def create_app(test_config=None):
    """
    Create and configure the application.
    """
    app = Flask('__name__', instance_relative_config=True)

    @app.route('/')
    def root():
        return 'Airbnb API, awaits creation.'

    return app

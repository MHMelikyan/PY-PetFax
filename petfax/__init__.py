from flask import Flask
from flask import (Blueprint)
# factory
def create_app():
    app = Flask(__name__)
    from . import pet
    @app.route('/')
    def hello():
        return 'Hello,PetFax!'
    #register pet blueprint
    app.register_blueprint(pet.bp)
    #return  the app
    return app


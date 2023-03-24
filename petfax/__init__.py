from flask import Flask

# factory
def create_app():
    app = Flask(__name__)
    from . import pet
    from . import fact
    
    #index
    @app.route('/')
    def hello():
        return 'Hello,PetFax!'

    #register pet blueprint
    app.register_blueprint(pet.bp)

    #register fact plueprint
    app.register_blueprint(fact.bp)

    #return  the app
    return app


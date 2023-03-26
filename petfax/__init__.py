from flask import Flask

# factory
def create_app():
    app = Flask(__name__)
    
    
    #index
    @app.route('/')
    def hello():
        return 'Hello,PetFax!'

    #register pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)

    #register fact plueprint
    from . import fact
    app.register_blueprint(fact.bp)

    #return  the app
    return app

